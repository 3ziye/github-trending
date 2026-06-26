# ShardX Launcher

<p align="center">
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-blue?style=flat-square"></a>
</p>

<p align="center">
  <a href="https://pypi.org/project/shardx/"><img alt="PyPI version" src="https://img.shields.io/pypi/v/shardx?style=flat-square&logo=pypi&logoColor=white&label=pypi&color=blue"></a>
  <a href="https://www.npmjs.com/package/@proxyshard/shardx"><img alt="npm version" src="https://img.shields.io/npm/v/@proxyshard/shardx?style=flat-square&logo=npm&logoColor=white&label=npm&color=red"></a>
  <a href="https://crates.io/crates/shardx"><img alt="crates.io version" src="https://img.shields.io/crates/v/shardx?style=flat-square&logo=rust&logoColor=white&label=crates.io&color=orange"></a>
  <a href="https://docs.rs/shardx"><img alt="docs.rs" src="https://img.shields.io/docsrs/shardx?style=flat-square&logo=docsdotrs&logoColor=white&label=docs.rs"></a>
</p>

<p align="center">
  <a href="https://github.com/ProxyShard/ShardBrowser/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/ProxyShard/ShardBrowser?style=flat-square&logo=github&label=Stars&color=lightgrey"></a>
  <a href="https://github.com/ProxyShard/ShardBrowser/commits"><img alt="Last commit" src="https://img.shields.io/github/last-commit/ProxyShard/ShardBrowser?style=flat-square&color=success"></a>
  <a href="https://pypi.org/project/shardx/"><img alt="PyPI downloads" src="https://img.shields.io/pypi/dm/shardx?style=flat-square&logo=pypi&logoColor=white&label=pypi&color=brightgreen"></a>
  <a href="https://www.npmjs.com/package/@proxyshard/shardx"><img alt="npm downloads" src="https://img.shields.io/npm/dt/@proxyshard/shardx?style=flat-square&logo=npm&logoColor=white&label=npm&color=brightgreen"></a>
  <a href="https://crates.io/crates/shardx"><img alt="crates.io downloads" src="https://img.shields.io/crates/d/shardx?style=flat-square&logo=rust&logoColor=white&label=crates.io&color=brightgreen"></a>
</p>

A project by the **[ProxyShard](https://proxyshard.com?utm_source=shardx&utm_medium=referral&utm_campaign=shardx-launcher)** team — the
proxy service with full **SOCKS5 UDP relay** (RFC 1928 §7) and active
**p0f TCP-fingerprint spoofing** on the exit (so the OS the proxy
claims to be on actually matches the SYN/ACK shape sites see). ShardX
is the in-house anti-detect browser stack we built to get the most out
of those proxies: the launcher manages profiles, binds proxies, and
ships the patched **Chromium 149** browser that does the actual
spoofing at the engine level.

* **Site:**     [https://proxyshard.com](https://proxyshard.com?utm_source=shardx&utm_medium=referral&utm_campaign=shardx-launcher)
* **Docs:**     [https://docs.proxyshard.com](https://docs.proxyshard.com?utm_source=shardx&utm_medium=referral&utm_campaign=shardx-launcher)
* **Usage:**    [https://docs.proxyshard.com/eng/usage-instructions/shardx-browser](https://docs.proxyshard.com/eng/usage-instructions/shardx-browser?utm_source=shardx&utm_medium=referral&utm_campaign=shardx-launcher)
* **UDP info:** [https://docs.proxyshard.com/eng/our-products/about-udp](https://docs.proxyshard.com/eng/our-products/about-udp?utm_source=shardx&utm_medium=referral&utm_campaign=shardx-launcher)
* **p0f info:** [https://docs.proxyshard.com/eng/our-products/p0f-spoofing](https://docs.proxyshard.com/eng/our-products/p0f-spoofing?utm_source=shardx&utm_medium=referral&utm_campaign=shardx-launcher)

Drive ShardX whichever way fits the job — all four read from the same
on-disk state, so a profile is reachable from every entry-point with
no sync step:

* **Desktop UI** — workspace for day-to-day work (profiles, proxies,
  cookies, fingerprint editor).
* **Local HTTP API** — Bearer-JWT auth on `127.0.0.1:40325`; create /
  start / stop profiles and grab a CDP endpoint from any language.
* **MCP server** — drops into Claude Desktop / Cursor for
  natural-language profile orchestration (HTTP API + browser-over-CDP).
* **Standalone SDKs** — Python, Node + Rust libraries that ship the engine
  themselves and need no GUI at all; ideal for scrapers / CI / servers.

Setup for each lives in [Usage](#usage) below.

<p align="center">
  <img src="docs/screenshots/00-launcher-workspace.jpg" alt="ShardX Launcher" width="820">
</p>

---

## What it is

**A free, open-source anti-detect browser for web scraping and
multi-accounting.**

Run hundreds of isolated browser identities side by side, each one a
fully-formed device with its own GPU, screen, fonts, audio stack,
timezone, locale, WebGL/WebGPU caps, TLS ClientHello, UA-CH, WebRTC
policy, geolocation and cookies — every signal coherent with the
others, and every signal **spoofed inside Chromium's C++ engine**
(Blink / V8 / network stack), not via JS injection that detectors trip
on instantly.

You get 170 ready-made device profiles out of the box (mac M1–M5,
Windows desktops/laptops with RTX/GTX/Intel/AMD GPUs, Linux
workstations), bind a SOCKS5 / HTTP proxy to each one, and the
l