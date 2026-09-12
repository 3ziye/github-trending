<p align="center">
  <img src="assets/logo.svg" width="96" alt="dsh-market logo">
</p>

# dsh-market

English | [中文](README.zh.md)

[![npm](https://img.shields.io/npm/v/dshmarket)](https://www.npmjs.com/package/dshmarket)
[![stars](https://img.shields.io/github/stars/dsh-market/dsh-market?style=flat)](https://github.com/dsh-market/dsh-market)

The plugin market inside DeepSeek Harness. Open Settings → **Plugin Market** → browse, search, one-click install.

![dsh-market](assets/demo-en.png)

One-click themes: install, switch live, no restart.

## Install

```sh
dsh plugin --profile web add dshmarket
```

Restart `dsh web`, then open **Settings → Plugin Market**.

**Requires dsh web 0.1.0-rc.6 or newer.** On an older host the market
disables itself and says so in the browser console rather than rendering
against primitives that are not there — if the Plugin Market entry never
appears, that is usually why. Worth checking when a desktop build bundles
its own dsh: it may be older than the one `npm` would give you (#139).

## What you get

- **Browse & search** the full community catalog (2300+ plugins, growing daily) — category filters, star counts, top/new sorting, bilingual descriptions that follow your UI language
- **Host-aware discovery** — cards show the DSH requirement declared by `engines.dsh` or lockstep `@deepseek-ai/dsh-*` peers; an opt-in filter hides only confirmed mismatches with the running host. Undeclared, malformed, unavailable, and GitHub-only entries remain visible rather than being guessed incompatible
- **Screenshots** — AppStore-style screenshots, auto-carousel when there's more than one, click to preview full-size: author-curated shots show right on the card (zero extra requests); plugins without curated shots fall back to automatic README extraction once you open the install dialog. Images load from GitHub hosting only
- **Comments** — every card opens the plugin's discussion thread in place. It is the same thread its pages on [dshmarket.com](https://dshmarket.com) and the [catalog](https://awesome-dsh-plugin.com) show, so a plugin has one conversation rather than three. Backed by GitHub Discussions through giscus: it loads when you open it, needs a GitHub account only to post, and the note above it says plainly that opening it contacts giscus.app and GitHub. On local dsh web, reading stays embedded while a dedicated GitHub action opens the exact discussion in a new tab for sign-in and posting, so the cross-site return never carries or depends on the host session
- **Favorites** — bookmark plugins and themes from Discover or the Themes tab; a dedicated Favorites tab lists them with search, sort, and install actions. Bookmarks persist in the profile's market state (`state.json`); entries that leave the catalog can be cleared in one click
- **Themes** — a dedicated tab for community themes and skins: install → active immediately, switch with one click (themes are mutually exclusive, your choice survives restarts), uninstall to revert
- **One-click install** — confirm the source, watch live progress; most plugins go live after a page refresh, no restart
- **Backup & restore** — export your profile's plugin list and configuration as readable JSON, import it on another machine, store it on WebDAV with daily auto-backup, or sync through a private GitHub Gist; restores **merge** (plugins installed after the backup are kept), validate before writing, and roll back on failure
- **Updates** — per-plugin update checks (npm version or pinned commit vs HEAD), one-click update, or update everything at once; the market updates itself the same way
- **Resilient GitHub routes** — in the China download region, Git refs, README content, and avatars each keep their own fallback order. The market remembers the last working route, switches only after transport/HTTP/payload validation fails, and rejects proxy error pages disguised as HTTP 200. If every built-in route fails, **Settings → Plugins → Plugin configuration → GitHub acceleration** accepts one persistent custom HTTPS prefix; `DSHM_GITHUB_PROXY` remains the operator-owned override
- **Public update API** — plugin-owned settings pages can use the versioned, capability-gated [update API v1](UPDATE-API-V1.md) (beta) instead of copying package-manager logic or depending on private Market UI responses
- **Uninstall** — two-step confirm; plugins installed this session are removed live
- **Hot disable / enable** — toggles write `- id: …` + `disabled: true|false` into the profile's `cordis.patch.yml` (the official patch layer, mechanism ported from [dsh-plugin-hub](https://github.com/Noob-stupid/dsh-plugin-hub)): DSH's HMR re-composes within ~1s, no restart, and the loader re-applies the choice on every boot; hand-edited patch rows show as badges, host-infrastructure plugins are protected from toggling, and a malformed patch file is never made worse
- **Restart when needed** — changes that cannot hot-load show a one-click restart beside the pending-change bann