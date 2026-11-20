# Exact

**The all-platform app framework. Agent native. Built for speed. No compromises.**

Exact is an **all-platform** framework for building real apps on the web, iOS, macOS, Android, and Linux — with Windows in active development, plus tvOS, watchOS, Android TV, and the terminal.

Exact is not a "cross-platform" framework. Cross-platform tools usually trade away each platform's strengths to maintain a lowest common denominator. Exact takes the opposite approach: build something **excellent on every platform on its own terms** — real DOM on the web, real UIKit on iOS, real AppKit on macOS, hardware-accelerated Material 3 rendering with native Android views on Android, and direct GPU/CPU rendering on Linux and Windows. Being **all-platform** is simply the side effect of getting every platform right from one source.

Everything in Exact is built around three priorities:

1. **[Agent Native](#1-agent-native)** — Built from the ground up so coding agents can build, run, see, operate, and verify real apps on every platform through one deterministic loop.
2. **[Speed is King](#2-speed-is-king)** — 100 ms cold starts, 100 ms edit-to-present reloads, zero app JavaScript before first pixel, and a ~20 KB web runtime, held to hard budgets.
3. **[No Compromises — Build Exactly What You Want](#3-no-compromises--build-exactly-what-you-want)** — Native platform controls with zero tells when you leave presentation unsaid; full creative control over layout, motion, graphics, shaders, and native platform objects whenever you want it.

> [!NOTE]
> Exact is pre-1.0 and changes daily. There is no packaged release, API stability guarantee, or backwards-compatibility layer yet — you build from a checkout of this repository.

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
    <td>UIKit views, native controls, and the system tab bar</td>
    <td>AppKit views and native controls</td>
  </tr>
</table>

<sub>One source, three platforms, captured by Exact's agent driver. <a href="https://github.com/expo/exact-templates/tree/main/softwear">Softwear</a> is a demo store from <a href="https://github.com/expo/exact-templates">exact-templates</a> (it displays Alternative Apparel's catalog, is not affiliated with that brand, and takes no orders or payments).</sub>

### Platforms

| Platform | Status | How it renders |
|---|---|---|
| **Web** | Works | Browser DOM (~20 KB runtime, zero layout engine shipped) |
| **iOS** | Works (Simulator & device) | UIKit views, native controls, and system bars |
| **macOS** | Works | AppKit views and native controls (no SwiftUI) |
| **Linux** | Works | Exact's GPU/CPU painter on DRM/KMS consoles or headless |
| **Android** | [Works](#android) (Material 3 polish in progress) | Hardware-accelerated Android Canvas (`RenderNode`) with Material 3 styling, native `EditText`, dialogs, and Compose date pickers |
| **Windows** | [Early](#early-windows) | DirectX 11 (`ink`) or CPU painter (neutral look + Fluent symbols) with native file dialogs, IME, and UI Automation |

The repository also ships **tvOS** and **watchOS** hosts, **Android TV** support in the Android APK, and a **terminal** host (`exact-terminal`) for command-line apps.

### Contents

- [Why Exact?](#why-exact)
  - [1. Agent Native](#1-agent-native)
  - [2. Speed is King](#2-speed-is-king)
  - [3. No Compromises — Build Exactly What You Want](#3-no-compromises--build-exactly-what-you-want)
  - [All-platform vs. cross-platform](#all-platform-vs-cross-platform)
- [Quick start](#quick-start)
- [The agent loop](#the-agent-loop)
- [How an Exact app is written](#how-an-exact-app-is-written)
- [How it works](#how-it-works)
- [Example apps](#example-apps)
- [What works today, and what doesn't yet](#what-works-today-and-what-doesnt-yet)
- [Building for iOS on Linux and WSL](#building-for-ios-on-linux-and-wsl)
- [Working on Exact](#working-on-exact)

---

## Why Exact?

### 1. Agent Native

Most frameworks bolt AI support on afterward with docs and wrapper scripts. Exact is designed around the agent loop so coding agents — and the humans directing them — can go from edit to verified native app on every platform without babysitting.

- **One driver operates every platform.** The same 10 operations (`tree`, `screenshot`, `tap`, `type`, `state`, `layout`, `logs`, `clock`, `prefer`, `perf`) drive the web, macOS, iOS Simulator, physical iPhones, Linux, Android, and Windows through `scripts/agent.mjs`.
- **Deterministic, seekable time.** In driven mode, time only advances when the driver moves 