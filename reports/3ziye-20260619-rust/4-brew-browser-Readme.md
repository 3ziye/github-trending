# Brew Browser

> A native macOS GUI for Homebrew — shipped in **two builds**.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Built with Tauri 2](https://img.shields.io/badge/Built%20with-Tauri%202-orange)](https://tauri.app)
[![Native: Swift + SwiftUI](https://img.shields.io/badge/Native-Swift%20%2B%20SwiftUI-blue?logo=swift&logoColor=white)](https://developer.apple.com/swiftui/)
[![macOS 13+](https://img.shields.io/badge/macOS-13%2B-lightgrey)](https://www.apple.com/macos)
[![Sponsor](https://img.shields.io/badge/♥-Sponsor-EC4899?logo=githubsponsors&logoColor=white)](https://github.com/sponsors/msitarzewski)

A small, fast desktop app for browsing, searching, installing, and snapshotting Homebrew packages. Full source, MIT-licensed, no telemetry, no accounts.

**Brew Browser comes in two builds that share one design and one data contract:**

- **Tauri build** — the cross-platform app: macOS 13+ (Ventura and up) **and** Linux. The shipping, signed-and-notarized download.
- **Native build** — a fully native **Swift 6 + SwiftUI + Liquid Glass** app for **macOS 26** (Tahoe). The "genuinely native" answer, ~half the memory.

Same features, same `brew` integration, same privacy posture — see [Two builds](#two-builds) below.

**Tauri build** (macOS 13+ · Linux)

![Brew Browser — Tauri build, Dashboard (dark)](docs/screenshots/dashboard-tauri.png)

**Native build** (Swift / SwiftUI · macOS 26)

![Brew Browser — native SwiftUI build, Dashboard (dark)](docs/screenshots/dashboard-native.png)

## Why this exists

Homebrew is the standard package manager on macOS. brew-browser gives it a real native GUI: browse what you have installed, search the full catalog, install / uninstall / upgrade with live output, snapshot your setup to a Brewfile and restore it on a new Mac. Trending packages come from Homebrew's published analytics. The whole thing is a thin, respectful frontend over the `brew` CLI itself.

## Features

- **Dashboard** — your Homebrew setup at a glance: installed count, updates available, brew version, formula/cask split, top-categories donut chart, storage usage (Cellar / Caskroom / var/log / cache) with one-click "Reveal in Finder" (macOS) / "Show in file manager" (Linux), and an opt-in **Exposure** card surfacing known vulnerabilities across your install
- **Library** — every installed formula and cask in one dense, filterable list, with outdated badges, sortable columns, category chip filters, an opt-in **Vulnerable** filter pill, inline severity dots, and a slide-over detail panel
- **Discover** — search the full Homebrew catalog (16k+ packages, bundled at build time + user-refreshable) by name, browse via the 19-category tile grid, and drill into subcategory groupings for large categories; multi-select chip filter
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

## Two builds

Brew Browser is maintained as **two implementations of the same app**, kept in
feature + data-contract parity. They are not competitors — they have different,
non-overlapping jobs, because SwiftUI does not run on Linux and Liquid Glass is
macOS-26-only.

| | **Tauri build** | **Native build** |
|---|---|---|
| Stack | Tauri 2 · SvelteKit · Rust | Swift 6 · SwiftUI · Liquid Glass |
| Runs on | **macOS 13+ and Linux** | **macOS 26 (Tahoe)** |
| Role | the shipping cross-platform app | the genuinely-native macOS flagship |
| Source | `src/` (frontend) + `src-tauri/` (Rust) | `native/` (Swift Package) |