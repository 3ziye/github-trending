<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="branding/wisp-wordmark-reverse.svg">
  <img src="branding/wisp-wordmark.svg" alt="Wisp" width="300">
</picture>

### Local-first, real-time meeting transcription — on-device, private, GPU-accelerated.

Your microphone **and** the meeting's audio become a live, per-speaker transcript with an AI copilot beside it — entirely on your machine. No cloud. No upload. No account.

<br>

[![CI](https://github.com/ppXD/Wisp/actions/workflows/ci.yml/badge.svg)](https://github.com/ppXD/Wisp/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/ppXD/Wisp?include_prereleases&sort=semver&label=release&color=c96442)](https://github.com/ppXD/Wisp/releases)
[![Platforms](https://img.shields.io/badge/platform-macOS%20·%20Windows-1a1915)](#-install)
[![Built with Rust](https://img.shields.io/badge/Rust-stable-c96442?logo=rust&logoColor=white)](https://www.rust-lang.org)
[![Tauri v2](https://img.shields.io/badge/Tauri-v2-1a1915?logo=tauri&logoColor=ffc131)](https://tauri.app)
[![License: MIT](https://img.shields.io/badge/license-MIT-5f8c6a)](#-license)

**English** · [简体中文](README.zh-Hans.md)

<br>

[![Download for macOS](https://img.shields.io/badge/Download-macOS%20·%20Apple%20Silicon-1a1915?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/ppXD/Wisp/releases)
&nbsp;
[![Download for Windows](https://img.shields.io/badge/Download-Windows%20x64-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/ppXD/Wisp/releases)

<br>

<img src="branding/screenshot-live.png" alt="Wisp — live transcription with per-speaker labels and the realtime AI Assist copilot" width="860">

</div>

---

**Wisp** turns any conversation into a clean, timestamped, speaker-labelled transcript in real time — and runs a live AI assistant alongside it. Every byte of audio and every model stays on your device by default. It installs in seconds, needs **zero** extra setup (no virtual audio drivers, no kernel extensions), and is tuned to the metal on each platform — Metal + the Neural Engine on Apple Silicon, native loopback on Windows.

> 🔒 **Private by design** · ⚡ **Optimized to the architecture** · 🎛️ **Yours to configure** · 🪶 **Install-and-go**

## ✨ Highlights

| | |
|---|---|
| 🎙️ **Live + AI copilot** | Sub-second streaming transcript with per-speaker labels, plus an AI assistant that summarizes, extracts action items, and coaches in real time |
| 🔒 **100% on-device** | Audio and models never leave your machine. Cloud engines are strictly opt-in, with your own keys |
| 🍎 **Apple-Silicon-native** | Metal GPU inference, Apple Neural Engine via Core ML, Unified Memory zero-copy, and on-device Apple SpeechAnalyzer |
| 🔌 **Zero dependencies** | One-click system-audio capture — **no BlackHole**, no kernel extensions, no virtual devices |
| 🎛️ **Truly customizable** | Choose, configure, and **delete** models freely. Language, accuracy/speed, decoding params — all in your hands |
| 📄 **SOTA file transcription** | Accurate batch transcription with diarization, word-level timestamps, custom vocabulary, and structured export |
| 🧠 **Private searchable memory** | Every meeting auto-saved to a local library you can search by **meaning**, not just keywords — on-device embeddings (Qwen3, BGE-M3, multilingual E5) with hybrid keyword + semantic ranking |
| 🪶 **Tiny footprint** | An 8–22 MB installer; multi-GB models stream in only when you ask for them |

---

## 🎙️ The live meeting copilot

This is the heart of Wisp — and it's fast.

- **Streaming transcript, sub-second.** Words appear as they're spoken (live partials → finalized lines), each timestamped. No "press stop to see the result."
- **Knows who's talking.** On-device diarization labels every line live — **You** vs **Them**, or **Speaker 1 / 2 / 3** — with running speaker centroids that stay stable across a long call.
- **Captures *both* sides.** Your microphone and the meeting's system audio are fused onto a single timeline, with **WebRTC AEC3 echo cancellation** so the remote voices don't bleed back through your mic. One click — no loopback driver to install.
- **🤖 AI Assist — your second brain in the call.** A live copilot panel that streams as it thinks:
  - **Rolling summaries**, **action items**, **decisions**, and **open questions** that update as the meeting unfolds
  - **Follow-up email** drafts, ready to send
  - **Real-time hints** and service-industry templates — sales coaching, support guidance, live sentiment/tone monitoring
  - Diarization-aware context so it knows *who* said *what*, with controlled cadence so it's helpful, not noisy

> Bring your own LLM endpoint (local or cloud) — the assistant is model-agnostic and fully parameterized (temperature, penalties, max tokens, and more).

## 📄 State-of-the-art file transcription

Drop in any audio or video file and get a transcript you can trust:

- **Accuracy-first by default** — Whisper **large-v3-t