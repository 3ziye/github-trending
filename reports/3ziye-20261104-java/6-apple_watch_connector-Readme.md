<p align="center">
  <img src="docs/assets/watch-companion-header.svg" alt="Apple Watch Companion — phone and desktop; Android, macOS, Linux and Windows" width="100%">
</p>

<h1 align="center">Apple Watch Companion</h1>

<p align="center">
  <strong>Android · macOS · Linux · Windows</strong><br>
  Native protocols. Physical hardware. A shared Companion.<br>
  Bluetooth · Pairing · IDS · Native Faces · Flutter · Java · Rust
</p>

<p align="center">
  <a href="#english"><img src="docs/assets/language-en.svg" alt="English" width="136" height="42"></a>
  &nbsp;
  <a href="#russian"><img src="docs/assets/language-ru.svg" alt="Русский" width="136" height="42"></a>
  &nbsp;
  <a href="https://www.youtube.com/watch?v=5zvBRTuSM30"><img src="docs/assets/video.svg" alt="Watch Android demo · Видео подключения к Android" width="224" height="42"></a>
  &nbsp;
  <a href="docs/DONATIONS.md"><img src="docs/assets/support.svg" alt="Support the developer · Поддержать разработчика" width="224" height="42"></a>
</p>

<p align="center">
  <a href="#en-start">Start here</a> · <a href="#en-calls">Call map</a> · <a href="#en-pairing">Pairing</a> · <a href="#en-api">API</a> · <a href="#en-build">Build</a> · <a href="#en-evidence">Evidence</a>
</p>

---

<a id="english"></a>

## English

<h2 align="center">⚠️ TESTED ONLY ON watchOS 26.2 (23S303)</h2>

**Android Magisk module:** [Download Bridge 0.2.427 ZIP](https://github.com/LordixDemon/apple_watch_connector/releases/download/magisk-0.2.427/apple-watch-bridge-magisk-0.2.427.zip) · [Installation](#en-android-install)

**Connect Apple Watch to Android, Linux and Windows through native Bluetooth/IDS protocols and a shared Flutter Companion. macOS uses the same interface with a limited Bluetooth backend.**

This project reconstructs the path from discovery and pairing to activation, reconnection, preference exchange, and native watch-face management. Companion presents observed Watch state and submits commands on all four platforms. Android Bridge owns the phone connection and keys. Linux and Windows use a Rust desktop backend, native HCI brokers and the shared Java protocol engine; macOS uses Rust and CoreBluetooth. Linux and Windows pairing uses the six-digit Watch code; camera pairing is available on Android.

Release preparation now has a shared Java `protocol-runtime` module, isolated
research/debug probes, Linux artifact auditing and shared Android distribution
signing. See the [release guide](docs/BUILD_AND_RELEASE.md). Fresh pairing,
activation and same-pair encrypted reconnect are physically verified on Linux
and Windows with the tested hardware; desktop application service coverage
remains partial.

The Linux Rust backend separates observed state, worker I/O/lifetime and command
routing. Stop/failure states reject late ready events; EOF and bounded cleanup
prevent stale readiness and abandoned workers. Portable Java modules share strict
dependency locks. Linux packages include a verified schema-2 inventory and use
deterministic archive metadata. See [stage 93](docs/REFACTOR_RELEASE_93.md).
Linux now exposes Bluetooth adapter selection in All Watches, remembers the
address across HCI index changes and requires reselection when saved hardware
is missing. See [adapter selection](docs/LINUX_ADAPTER_SELECTION_94.md).

> **Documentation snapshot: October 13, 2026.** The main verified hardware is Apple Watch Ultra 2, `Watch7,5`, watchOS `26.2 / 23S303`. Source versions: Bridge **0.2.429 / code 629**, Companion **1.0.86+87**, Rust workspace **0.1.1**. Source versions do not establish installed device versions. Android camera pairing, Linux pairing on Mint 22.3 and Windows pairing on Windows 10 / Realtek `0bda:b00e` have separate hardware verification.

Development is ongoing. The hardware journal confirms camera pairing, activation, and a visible Watch face. Full Watch.app parity, every iPhone feature, and compatibility with every Apple Watch model remain incomplete. macOS discovery is implemented; the complete physical pairing → activation → IDS path is unfinished.

## Contents

- [Capabilities and verification boundaries](#en-status)
- [Project layout](#en-layout)
- [System architecture](#en-architecture)
- [End-to-end call map](#en-calls)
- [Protocol stack](#en-stack)
- [Fresh pairing, step by step](#en-pairing)
- [Activation and Setup completion](#en-setup)
- [Operational reconnection](#en-reconnect)
- [Complete Companion → Bridge API registry](#en-api)
- [IDS routes and handlers](#en-routes)
- [Native faces: read, mutate, import, resources](#en-faces)
- [Settings, pigments, and monograms](#en-preferences)
- [Notifications, finding devices, Wi-Fi, and Health](#en-features)
- [Modern StateReplicator and QUIC](#en-replicator)
- [Keys, storage, and ownership](#en-ownership)
- [Start from a clean machine](#en-start)
- [Build, test, and first run](#en-build)
- [macOS discovery build](#en-macos)
- [Linux connection and adapter selection](#en-linux)
- [Windows connection](#en-windows)
- 