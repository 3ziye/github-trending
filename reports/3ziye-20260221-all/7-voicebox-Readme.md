<p align="center">
  <img src=".github/assets/icon-dark.webp" alt="Voicebox" width="120" height="120" />
</p>

<h1 align="center">Voicebox</h1>

<p align="center">
  <strong>The open-source voice synthesis studio.</strong><br/>
  Clone voices. Generate speech. Build voice-powered apps.<br/>
  All running locally on your machine.
</p>

<p align="center">
  <a href="https://github.com/jamiepine/voicebox/releases">
    <img src="https://img.shields.io/github/downloads/jamiepine/voicebox/total?style=flat&color=blue" alt="Downloads" />
  </a>
  <a href="https://github.com/jamiepine/voicebox/releases/latest">
    <img src="https://img.shields.io/github/v/release/jamiepine/voicebox?style=flat" alt="Release" />
  </a>
  <a href="https://github.com/jamiepine/voicebox/stargazers">
    <img src="https://img.shields.io/github/stars/jamiepine/voicebox?style=flat" alt="Stars" />
  </a>
  <a href="https://github.com/jamiepine/voicebox/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/jamiepine/voicebox?style=flat" alt="License" />
  </a>
</p>

<p align="center">
  <a href="https://voicebox.sh">voicebox.sh</a> •
  <a href="#download">Download</a> •
  <a href="#features">Features</a> •
  <a href="#api">API</a> •
  <a href="#roadmap">Roadmap</a>
</p>

<br/>

<p align="center">
  <a href="https://voicebox.sh">
    <img src="landing/public/assets/app-screenshot-1.webp" alt="Voicebox App Screenshot" width="800" />
  </a>
</p>

<p align="center">
  <em>Click the image above to watch the demo video on <a href="https://voicebox.sh">voicebox.sh</a></em>
</p>

<br/>

<p align="center">
  <img src="landing/public/assets/app-screenshot-2.webp" alt="Voicebox Screenshot 2" width="800" />
</p>

<p align="center">
  <img src="landing/public/assets/app-screenshot-3.webp" alt="Voicebox Screenshot 3" width="800" />
</p>

<br/>

## What is Voicebox?

Voicebox is a **local-first voice cloning studio** with DAW-like features for professional voice synthesis. Think of it as a **local, free and open-source alternative to ElevenLabs** — download models, clone voices, and generate speech entirely on your machine.

Unlike cloud services that lock your voice data behind subscriptions, Voicebox gives you:

- **Complete privacy** — models and voice data stay on your machine
- **Professional tools** — multi-track timeline editor, audio trimming, conversation mixing
- **Model flexibility** — currently powered by Qwen3-TTS, with support for XTTS, Bark, and other models coming soon
- **API-first** — use the desktop app or integrate voice synthesis into your own projects
- **Native performance** — built with Tauri (Rust), not Electron
- **Super fast on Mac** — MLX backend with native Metal acceleration for 4-5x faster inference on Apple Silicon

Download a voice model, clone any voice from a few seconds of audio, and compose multi-voice projects with studio-grade editing tools. No Python install required, no cloud dependency, no limits.

---

## Download

Voicebox is available now for macOS and Windows.

| Platform | Download |
|----------|----------|
| macOS (Apple Silicon) | [voicebox_aarch64.app.tar.gz](https://github.com/jamiepine/voicebox/releases/download/v0.1.0/voicebox_aarch64.app.tar.gz) |
| macOS (Intel) | [voicebox_x64.app.tar.gz](https://github.com/jamiepine/voicebox/releases/download/v0.1.0/voicebox_x64.app.tar.gz) |
| Windows (MSI) | [voicebox_0.1.0_x64_en-US.msi](https://github.com/jamiepine/voicebox/releases/download/v0.1.0/voicebox_0.1.0_x64_en-US.msi) |
| Windows (Setup) | [voicebox_0.1.0_x64-setup.exe](https://github.com/jamiepine/voicebox/releases/download/v0.1.0/voicebox_0.1.0_x64-setup.exe) |

> **Linux builds coming soon** — Currently blocked by GitHub runner disk space limitations.

---

## Features

### Voice Cloning with Qwen3-TTS

Powered by Alibaba's **Qwen3-TTS** — a breakthrough model that achieves near-perfect voice cloning from just a few seconds of audio.

- **Instant cloning** — Upload a sample, get a voice profile
- **High fidelity** — Natural prosody, emotion, and cadence
- **Multi-language** — English, Chinese, and more coming
- **Lightning fast on Mac** — MLX backend leverages Apple Silicon's Neural Engine for super fast generation

### Voice Profile Management

- **Create profiles** from audio files or record directly in-app
- **Import/Export** profiles to share or backup
- **Multi-sample support** — combine multiple samples for higher quality cloning
- **Organize** with descriptions and language tags

### Speech Generation

- **Text-to-speech** with any cloned voice
- **Batch generation** for long-form content
- **Smart caching** — regenerate instantly with voice prompt caching

### Stories Editor

Create multi-voice narratives, podcasts, and conversations with a timeline-based editor.

- **Multi-track composition** — arrange multiple voice tracks in a single project
- **Inline audio editing** — trim and split clips directly in the timeline
- **Auto-playback** — preview stories with synchronized 