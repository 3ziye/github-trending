# brew-browser

> A native macOS GUI for Homebrew.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Built with Tauri 2](https://img.shields.io/badge/Built%20with-Tauri%202-orange)](https://tauri.app)
[![macOS 13+](https://img.shields.io/badge/macOS-13%2B-lightgrey)](https://www.apple.com/macos)
[![Sponsor](https://img.shields.io/badge/♥-Sponsor-EC4899?logo=githubsponsors&logoColor=white)](https://github.com/sponsors/msitarzewski)

A small, fast desktop app for browsing, searching, installing, and snapshotting Homebrew packages. Full source, MIT-licensed, no telemetry, no accounts.

![brew-browser — Dashboard (dark)](docs/screenshots/dashboard-dark.png)

## Why this exists

Homebrew is the standard package manager on macOS. brew-browser gives it a real native GUI: browse what you have installed, search the full catalog, install / uninstall / upgrade with live output, snapshot your setup to a Brewfile and restore it on a new Mac. Trending packages come from Homebrew's published analytics. The whole thing is a thin, respectful frontend over the `brew` CLI itself.

## Features

- **Dashboard** — your Homebrew setup at a glance: installed count, updates available, brew version, formula/cask split, top-categories donut chart, storage usage (Cellar / Caskroom / var/log / cache) with one-click "Reveal in Finder", and an opt-in **Exposure** card surfacing known vulnerabilities across your install
- **Library** — every installed formula and cask in one dense, filterable list, with outdated badges, sortable columns, category chip filters, an opt-in **Vulnerable** filter pill, inline severity dots, and a slide-over detail panel
- **Discover** — search the full Homebrew catalog (15,974 packages, bundled at build time + user-refreshable) by name or browse via the 19-category tile grid; multi-select chip filter
- **Trending** — top packages from Homebrew's published `formulae.brew.sh` analytics, with 30 / 90 / 365-day windows, sortable columns, a **velocity index** (recent-month vs prior-11-month adoption signal), and opt-in per-package install-trend sparklines
- **Snapshots** — save and restore Brewfiles using Homebrew's own `brew bundle` mechanism; "set up a new Mac" in one click
- **Services** — list, start, stop, and restart background services managed by launchd through `brew services`
- **Security** — opt-in vulnerability scanning. Surfaces known CVEs against your installed formulae via the official `brew vulns` subcommand (OSV.dev), with optional GHSA enrichment when you're signed into GitHub. Inline severity dots, per-package Security card with "Upgrade to fix" wired to the existing upgrade pipeline. Off by default; one-click installer for `brew vulns` itself when you opt in
- **Activity** — every `brew` invocation streams live into a bottom drawer with full stdout/stderr; session history persists across launches (last 200 jobs, capped lines)

A global Cmd+K command palette covers the verbs. Cmd+0 returns to the Dashboard; Cmd+1…6 jumps between sections. Cmd+, opens Settings. Click the 🍺 brand to return home. Window dragging works from any panel header (native macOS overlay title bar + NSVisualEffectView vibrancy).

## What this isn't

- Not a Homebrew replacement — every action shells out to the real `brew` CLI
- Not telemetry-funded — no analytics, no accounts, no phone-home
- Not freemium — there is no paid tier, because there is no tier

## Install (end users)

**Direct download (recommended):** grab the latest signed + notarized `.dmg` from the [releases page](https://github.com/msitarzewski/brew-browser/releases/latest), open it, and drag **brew-browser** to your Applications folder. No Gatekeeper warning. This is the build that's signed and tested directly each release, and it keeps you on the app's own verified updater (Settings → Network → Updates).

**Homebrew:**

```sh
brew tap msitarzewski/brew-browser
brew install --cask brew-browser
```

Installs the same notarized `.dmg`. Update later with `brew upgrade --cask brew-browser`.

Apple Silicon only for now. macOS 13 (Ventura) or newer.

## Build from source

Prereqs:

- [Rust](https://rustup.rs/) (stable, edition 2021+)
- [Node.js 22+](https://nodejs.org/) and npm
- [Homebrew](https://brew.sh/) itself
- Xcode Command Line Tools: `xcode-select --install`

Then:

```sh
git clone https://github.com/msitarzewski/brew-browser
cd brew-browser
npm install
npm run tauri dev      # development with HMR
npm run tauri build    # produces a .dmg in src-tauri/target/release/bundle/
```

## Architecture

A Tauri 2 shell hosts a SvelteKit + Svelte 5 frontend in the system WebView. A Rust backend exposes ~55 typed Tauri commands that shell out to `brew` via `tokio::process` and stream stdout/stderr back over typed IPC channels. The full Homebrew catalog is bundled at build time (~6 MiB gzipped) and refreshable on demand. Trending data comes straight from `formulae.brew.sh`'s public analytics JSON, cached in memory for an hour. Optio