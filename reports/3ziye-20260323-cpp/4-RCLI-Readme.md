<p align="center">
  <img src="assets/rcli_waveform.gif" alt="RCLI Waveform" width="700" />
  <br>
  <strong>Talk to your Mac, query your docs, no cloud required.</strong>
  <br><br>
  <a href="https://github.com/RunanywhereAI/RCLI"><img src="https://img.shields.io/badge/platform-macOS-blue" alt="macOS"></a>
  <a href="https://github.com/RunanywhereAI/RCLI"><img src="https://img.shields.io/badge/chip-Apple_Silicon-black" alt="Apple Silicon"></a>
  <a href="https://github.com/RunanywhereAI/RCLI"><img src="https://img.shields.io/badge/inference-100%25_local-green" alt="Local"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT"></a>
</p>

**RCLI** is an on-device voice AI for macOS. A complete STT + LLM + TTS + VLM pipeline running natively on Apple Silicon — 40 macOS actions via voice, local RAG over your documents, on-device vision (camera & screen analysis), sub-200ms end-to-end latency. No cloud, no API keys.

Powered by [MetalRT](#metalrt-gpu-engine), a proprietary GPU inference engine built by [RunAnywhere, Inc.](https://runanywhere.ai) specifically for Apple Silicon.

## Demo

> Real-time screen recordings on Apple Silicon — no cloud, no edits, no tricks.

<table>
<tr>
<td width="50%" align="center">
<strong>Voice Conversation</strong><br>
<em>Talk naturally — RCLI listens, understands, and responds on-device.</em><br><br>
<a href="https://youtu.be/qeardCENcV0">
<img src="assets/demos/demo1-voice-conversation.gif" alt="Voice Conversation Demo" width="100%">
</a>
<br><sub>Click for full video with audio</sub>
</td>
<td width="50%" align="center">
<strong>App Control</strong><br>
<em>Control Spotify, adjust volume — 38 macOS actions by voice.</em><br><br>
<a href="https://youtu.be/eTYwkgNoaKg">
<img src="assets/demos/demo2-spotify-volume.gif" alt="App Control Demo" width="100%">
</a>
<br><sub>Click for full video with audio</sub>
</td>
</tr>
<tr>
<td width="50%" align="center">
<strong>Models</strong><br>
<em>Browse models, hot-swap LLMs — all from the TUI.</em><br><br>
<a href="https://youtu.be/HD1aS37zIGE">
<img src="assets/demos/demo3-benchmarks.gif" alt="Models & Benchmarks Demo" width="100%">
</a>
<br><sub>Click for full video with audio</sub>
</td>
<td width="50%" align="center">
<strong>Document Intelligence (RAG)</strong><br>
<em>Ingest docs, ask questions by voice — ~4ms hybrid retrieval.</em><br><br>
<a href="https://youtu.be/8FEfbwS7cQ8">
<img src="assets/demos/demo4-rag-documents.gif" alt="RAG Demo" width="100%">
</a>
<br><sub>Click for full video with audio</sub>
</td>
</tr>
</table>

## Install

> [IMPORTANT]
> **Requires macOS 13+ on Apple Silicon. MetalRT engine requires M3 or later.** M1/M2 Macs fall back to llama.cpp automatically.

**One command:**

```bash
curl -fsSL https://raw.githubusercontent.com/RunanywhereAI/RCLI/main/install.sh | bash
```

**Or via Homebrew:**

```bash
brew tap RunanywhereAI/rcli https://github.com/RunanywhereAI/RCLI.git
brew install rcli
rcli setup          # required — downloads AI models (~1GB, one-time)
```

**Upgrade to latest:**

```bash
brew update
brew upgrade rcli
```

<details>
<summary><strong>Troubleshooting: SHA256 mismatch or stale version</strong></summary>

If `brew install` or `brew upgrade` fails with a checksum error:

```bash
# Force-refresh the tap to pick up the latest formula
cd $(brew --repo RunanywhereAI/rcli) && git fetch origin && git reset --hard origin/main
brew reinstall rcli
```

If that doesn't work, clean re-tap and clear the download cache:

```bash
brew untap RunanywhereAI/rcli
rm -rf "$(brew --cache)/downloads/"*rcli*
brew tap RunanywhereAI/rcli https://github.com/RunanywhereAI/RCLI.git
brew install rcli
rcli setup
```

</details>

## Quick Start

```bash
rcli                             # interactive TUI (push-to-talk + text)
rcli listen                      # continuous voice mode
rcli ask "open Safari"           # one-shot command
rcli ask "play some jazz on Spotify"
rcli vlm photo.jpg "what's in this image?"  # vision analysis
rcli camera                      # live camera VLM
rcli screen                      # screen capture VLM
rcli metalrt                     # MetalRT GPU engine management
rcli llamacpp                    # llama.cpp engine management
```


## Benchmarks

<p align="center">
  <img src="assets/decode-vs-llamacpp.webp" alt="MetalRT vs llama.cpp decode speed" width="700" />
  <br>
  <em>MetalRT decode throughput vs llama.cpp and Apple MLX on Apple M3 Max</em>
</p>

<p align="center">
  <img src="assets/rtf_comparison.webp" alt="STT and TTS real-time factor comparison" width="700" />
  <br>
  <em>STT and TTS real-time factor — lower is better. MetalRT STT is 714x faster than real-time.</em>
</p>

For More info : 
- https://www.runanywhere.ai/blog/metalrt-fastest-llm-decode-engine-apple-silicon
- https://www.runanywhere.ai/blog/metalrt-speech-fastest-stt-tts-apple-silicon
- https://www.runanywhere.ai/blog/fastvoice-on-device-voice-ai-pipeline-apple-silicon

## Feature