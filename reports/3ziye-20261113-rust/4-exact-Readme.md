# Exact

**Write an app once. It runs natively on the web, macOS, iOS, and Linux, and an AI
agent can build it, run it, see it, and test it on every one of them.**

**Building an app?** With the tools installed ([Quick start, step 1](#1-install-the-tools)),
run `bun scripts/exact.mjs setup` once, make the app with `bun scripts/exact.mjs new <path>`,
and read [`docs/start-here.md`](docs/start-here.md) (for a website,
[`docs/start-here-site.md`](docs/start-here-site.md)): that guide is the only required
reading. The rest of this page describes Exact for people deciding whether to use it
or working on it.

> [!TIP]
> **Try it with a coding agent.** On a Mac with Xcode, Rust, Bun, and Chrome installed,
> give Claude Code this prompt:
>
> ```text
> Clone https://github.com/expo/exact and follow its README to make a new Exact
> app with `exact new`. Run `bun scripts/exact.mjs setup` once first. Make a todo
> list where I can add items, check them off, delete them,
> and see how many are left. Put the view in Contract and keep the list in `app.ts`.
> Write an `app.test.contract`, pass it on web, macOS, and the iOS Simulator with
> `scripts/agent.mjs`, then open the app for me on all three.
> ```
>
> A fresh agent given the earlier version of this prompt on a clean clone (2026-10-04, Hermes already in the
> machine cache, Cargo's cache warm) finished in about 57 minutes, and its tests passed
> on all three platforms. About 25 of those minutes were the first macOS and iOS builds,
> roughly 13 minutes each; later builds take a minute or two. On a machine that has
> lacked Hermes, its source build came first and added time. Current setup downloads and
> verifies the pinned host/iOS bundles once instead; ordinary builds stay offline.

<table>
  <tr>
    <th>Web</th>
    <th>iOS</th>
    <th>macOS</th>
  </tr>
  <tr valign="top">
    <td><img src="docs/screenshots/softwear-web.webp" width="360" alt="Softwear's hoodies page in Chrome"></td>
    <td><img src="docs/screenshots/softwear-ios.webp" width="160" alt="Softwear's hoodies page as a native iOS app"></td>
    <td><img src="docs/screenshots/softwear-macos.webp" width="290" alt="Softwear's hoodies page as a native macOS app"></td>
  </tr>
  <tr valign="top">
    <td>The browser's own DOM and CSS</td>
    <td>UIKit views, native controls and the system's tab bar</td>
    <td>AppKit views and native controls</td>
  </tr>
</table>

<sub>One <code>app.contract</code>, the same screen on three hosts, captured by the agent driver. <a href="https://github.com/expo/exact-templates/tree/main/softwear">Softwear</a> is a demonstration store you can generate from <a href="https://github.com/expo/exact-templates">exact-templates</a>: it shows Alternative Apparel's catalog, is not affiliated with that brand, and takes no real orders or payments.</sub>

Exact is a cross-platform application runtime. You describe your interface in
**Contract**, a small declarative language, and you write your data logic in
**TypeScript or Rust**. The Contract compiler turns the interface into a compact
*plan*. On the web, that plan becomes one ES module over a ~20 KB runtime that drives
the real DOM. On macOS, iOS, and Linux, a Rust runner executes the same plan, a Rust
layout kernel computes every box with CSS rules, and each platform draws with its own
tools: AppKit, UIKit, or a GPU painter. There is no webview and no JavaScript bridge
in the UI, and no app JavaScript runs before the first pixel.

> [!NOTE]
> Exact is pre-1.0 and changes daily. There is no API stability, no backwards
> compatibility, and no migration guide, by design (`rules/DEFERRED.md`). This
> repository, `exact2`, is a rebuild of an earlier one ("exact1"), whose design
> documents are research, never authority.

The design record is a separate, private repository of numbered documents (LLPs),
`expo/exact-llp`, which those with access clone into `llp/` (git ignores it). This
README and the guides cite it by number (`LLP 1115 D7`). The guides under [`docs/`](docs)
are the public documentation.

Upgrade note (2026-10-16): Snapback mutation replies with `ok: false` now throw
`refused(why)` and expose `failure(slot)`; see the
[before/after and inherited-app commands](snapback4/README.md#updating-an-inherited-app).

## Contents

- [Three principles](#three-principles)
- [How it works](#how-it-works)
- [Quick start](#quick-start)
- [Contract](#contract)
- [Example apps](#example-apps)
- [What works today, and what doesn't yet](#what-works-today-and-what-doesnt-yet)
- [Repository map](#repository-map)
- [Working on Exact](#working-on-exact)

## Three principles

### 1. Agent native

Exact assumes much of the code will be written by AI agents. An agent can make an app,
run it, look at it, operate it, and prove it works without a person in the loop.

- **Ten operations, the same on every host.** `tree · screenshot · tap · type · state
  · layout · logs · clock · prefer · perf` drive the web, macOS, iOS (Simulator or a real
  iPhone), and