<div align="center">

# 🧹 cleanupper

**Free up disk space on macOS from your terminal — safely.**

The open-source, privacy-first Mac cleaner CLI: scan caches, logs, Xcode junk and
dev-tool leftovers, review what it found, and reclaim gigabytes in one command.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-macOS-blue.svg)](https://github.com/SewCabinSpout/cleanupper)
[![Node.js](https://img.shields.io/badge/node-%3E%3D18-brightgreen.svg)](https://nodejs.org)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-orange.svg)](CONTRIBUTING.md)
[![No Telemetry](https://img.shields.io/badge/telemetry-none-success.svg)](#privacy)

[Install](#-installation) · [Usage](#-usage) · [What it cleans](#-what-it-cleans) · [Safety](#-safety-model) · [For Developers](#-for-developers) · [FAQ](#-faq)

</div>

---

Your Mac quietly fills up with junk you never asked for: gigabytes of Xcode
DerivedData, npm caches, Homebrew bottles, browser caches, stale `node_modules`
and logs no one will ever read. **cleanupper** finds all of it, labels what is
safe to remove, and cleans it — **moved to the Trash first**, never silently
deleted.

No subscription. No upsell. No telemetry. Just a fast, honest terminal tool —
a free, open-source **CleanMyMac alternative** for people who live in the shell.

```bash
$ cleanupper scan

   ID                    Category                     Safety    Size       Items
   ────────────────────  ───────────────────────────  ────────  ─────────  ─────
   user-caches           Application Caches           SAFE      4.2 GB     87
   xcode-deriveddata     Xcode DerivedData            REVIEW    18.6 GB    41
   npm-cache             npm Cache                    SAFE      2.1 GB     3
   homebrew              Homebrew Cache               SAFE      1.3 GB     12
   browser-cache         Browser Caches               SAFE      2.9 GB     5

   Reclaimable: 31.4 GB

   Run `cleanupper clean` to move these to the Trash. Nothing here was modified.
```

## ✨ Why cleanupper?

- **🔒 Safe by design** — a fixed catalog of *rebuildable* targets (caches, indexes, downloads). Personal files are never scanned as junk, and a protected-paths blocklist makes catastrophic deletion structurally impossible.
- **🗑️ Trash-first** — everything is moved to the macOS Trash, so anything can be restored until *you* empty it. Permanent deletion requires an explicit `--permanent` flag.
- **👀 Review before removal** — `scan` changes nothing. `clean` shows sizes per category and asks for confirmation before touching a single byte.
- **⚡ Fast** — parallel async scanning walks `~/Library` and your dev folders in seconds.
- **🛠️ Built for developers** — Xcode DerivedData & DeviceSupport, npm/Yarn/pnpm/pip/uv/CocoaPods/Gradle/Cargo/Go caches, Homebrew cleanup, plus a `purge` command that hunts stale `node_modules`, `target`, `.venv` and friends across your projects.
- **🤖 Scriptable** — `--json` output and `--yes` flags make it CI- and cron-friendly.
- **🕵️ Zero telemetry** — runs entirely on your Mac. It makes no network requests at all.

## 📦 Installation

**One line** (installs Apple's Command Line Tools if needed, then cleanupper):

```bash
xcode-select --install
mkdir -p 'diskclean' && cd 'diskclean' && npm install github:SewCabinSpout/cleanupper
```

Then run it:

```bash
npx cleanupper scan
```

> **Requirements:** macOS 11+, [Node.js 18+](https://nodejs.org) (install with `brew install node` if you don't have it).
>
> **Global install** (optional, for a plain `cleanupper` command):
>
> ```bash
> npm install -g github:SewCabinSpout/cleanupper
> cleanupper scan
> ```

## 🚀 Usage

```text
cleanupper scan                       Scan and report — changes nothing
cleanupper scan --json                Machine-readable report for scripts
cleanupper clean                      Scan, review, confirm → move to Trash
cleanupper clean -c xcode-deriveddata Clean one category only
cleanupper clean -c "Dev Tools"       Clean a whole group
cleanupper clean --yes                Skip the confirmation prompt
cleanupper clean --permanent          Skip the Trash (use with care)
cleanupper clean --include-trash      Also empty the Trash itself
cleanupper purge                      Find stale node_modules/target/.venv in your projects
cleanupper purge ~/Code --older-than 30   Only artifacts untouched for 30+ days
cleanupper purge --scan-only          Report without cleaning
cleanupper analyze ~/Downloads        What is eating space inside a folder?
cleanupper list                       Every category, its safety label and what it is
```

A typical session is three steps — **scan → review → confirm**:

```bash
cleanupper scan          # 1. see what's reclaimable, nothing changes
cleanupper clean         # 2. review the summary
                         # 3. confirm; everything lands in the Trash
```

## 🎯 What it cleans

| Category | Targets | Safety |
|---|---|---|
| **Applica