# invisible_playwright

[![tests](https://github.com/feder-cr/invisible_playwright/actions/workflows/tests.yml/badge.svg)](https://github.com/feder-cr/invisible_playwright/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Firefox 150.0.1](https://img.shields.io/badge/firefox-150.0.1-orange.svg)](https://www.mozilla.org/firefox/)
[![GitHub release](https://img.shields.io/github/v/release/feder-cr/invisible_playwright.svg)](https://github.com/feder-cr/invisible_playwright/releases)
[![GitHub stars](https://img.shields.io/github/stars/feder-cr/invisible_playwright.svg?style=social)](https://github.com/feder-cr/invisible_playwright/stargazers)
[![browser launches](https://img.shields.io/github/downloads/feder-cr/invisible_firefox/usage-counter/total?label=browser%20launches&color=blue)](https://github.com/feder-cr/invisible_firefox/releases/tag/usage-counter)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Federico%20Elia-0A66C2?logo=linkedin&logoColor=white)](https://it.linkedin.com/in/federico-elia-5199951b6)

**Stealth Firefox that passes every bot detection test. Drop-in Playwright replacement, fingerprint patched at the C++ level, not a JavaScript shim.**

![invisible_playwright - 5/5 detection suites passed](docs/screenshots/hero.gif)


## Why it's powerful

**This is the actively maintained Firefox-based anti-detect browser in 2026.** Camoufox pioneered the source-level patched Firefox approach, but the project has been in a roughly year-long maintenance gap and its base Firefox version is now several majors behind. CloakBrowser does the same thing for Chromium and works well, but it still hits the Chromium reCAPTCHA ceiling (~0.3-0.5). `invisible_playwright` ships **Firefox 150** with weekly releases, source-level C++ patches end-to-end, and a measured **0.90 reCAPTCHA v3** score.

**Most other anti-detect browsers patch Chromium at the JavaScript level** - they override `navigator`, `WebGLRenderingContext.getParameter`, canvas APIs, and so on via injected scripts. This has two fatal problems:

1. **JS patches are detectable.** Anti-bots enumerate native function `.toString()`, check descriptor configurability, compare property enumeration order, watch for prototype mutations. Every patch leaves a fingerprint of its own. CreepJS has an entire battery of "lies detectors" built around this.
2. **Chromium itself is now suspect.** Residential-proxy bot traffic is overwhelmingly Chromium-based, so detectors weight anything Chromium-shaped as risky by default. Chromium-based forks inherit Chrome's open-source layers (BoringSSL, Blink, V8, ANGLE) cleanly, but they still cannot fully match Chrome in practice: Chrome ships closed-source components on top (Widevine, proprietary codecs, Google Update / Safe Browsing endpoints) that flip detectable JS feature flags and network signals, and forks lag Chrome's release cadence by days to weeks, leaving telltale version-specific behaviours that detectors lock onto.

**invisible_playwright patches Firefox at the C++ level.** The spoofed values come back out through the normal Gecko paths - there is no JS shim, no override, no `Object.defineProperty`. **From the page's point of view, the browser is just telling the truth.** Anti-bot lie-detectors have nothing to latch onto.

invisible_playwright spoofs **all the layers that matter, together, coherently**: Navigator, screen, GPU/WebGL, Canvas, fonts, audio, WebRTC, timezone, DevTools detection, SOCKS5 auth, and the rest. See [feder-cr/invisible_firefox](https://github.com/feder-cr/invisible_firefox) for the full per-layer breakdown of which C++ files are patched and why.

Everything is driven by preferences - no hardcoded values in the binary. You change one pref, you change the spoofed value.

---

## How it compares

The closest peer in the source-level patching space is **Camoufox** (Firefox, open source): same approach as ours, but in a roughly year-long maintenance gap with its base Firefox several majors behind. **CloakBrowser** ships a similar pitch for Chromium, but its binary is **closed source** (the source-level patches are not published, you only get the compiled output), and it still hits the Chromium reCAPTCHA ceiling. The commercial anti-detect browsers (**Multilogin**, **GoLogin**, AdsPower, Dolphin, Kameleo) are paid SaaS that overlay JS-layer spoofing on a patched Chromium. Managed profiles are nice but raw detection bypass sits below both Camoufox and us.

| | invisible_playwright | Camoufox | CloakBrowser | Multilogin | GoLogin |
|---|---|---|---|---|---|
| Engine | Firefox 150 | Firefox (~1 year old base) | Chromium | Chromium fork | Chromium fork |
| Patch depth | C++ source | C++ source | C++ source (binary only) | JS overrides | JS overrides |
| Maintenance | Active (weekly) | Gap (~1 year) | Active | Active SaaS | Active SaaS |
|