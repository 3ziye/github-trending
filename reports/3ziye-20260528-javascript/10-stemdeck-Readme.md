<div align="center">

<img src="imgs/stemdeck-svg-assets/stemdeck-logo-stacked.svg" alt="StemDeck" width="515" />

**Free, local stem separation. No account. No upload. No subscription.**

<div align="center">
  <a href="https://ci.popchores.app/repos/2"><img src="https://ci.popchores.app/api/badges/2/status.svg?event=push" alt="CI"></a>
  <a href="https://github.com/stemdeckapp/stemdeck/stargazers"><img src="https://img.shields.io/github/stars/stemdeckapp/stemdeck?style=flat-square" alt="GitHub Stars"></a>
  <a href="https://github.com/stemdeckapp/stemdeck/releases"><img src="https://img.shields.io/github/downloads/stemdeckapp/stemdeck/total?style=flat-square&color=52c65f" alt="Total Downloads"></a>
  <a href="https://github.com/stemdeckapp/stemdeck/releases/latest"><img src="https://img.shields.io/github/v/release/stemdeckapp/stemdeck?style=flat-square" alt="Latest Release"></a>
  <a href="https://github.com/stemdeckapp/stemdeck/blob/main/LICENSE"><img src="https://img.shields.io/github/license/stemdeckapp/stemdeck?style=flat-square" alt="License"></a>
</div>

<br>

<p align="center"><sub>JOIN THE COMMUNITY</sub></p>
<div align="center">
  <a href="https://github.com/stemdeckapp/stemdeck"><img src="https://img.shields.io/badge/GitHub-stemdeckapp-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub"></a>
  <a href="https://discord.gg/2MVsWqaPRe"><img src="https://img.shields.io/badge/Discord-Join-5865F2?style=flat-square&logo=discord&logoColor=white" alt="Discord"></a>
  <a href="https://www.reddit.com/r/StemDeckApp/"><img src="https://img.shields.io/badge/Reddit-r%2FStemDeckApp-FF4500?style=flat-square&logo=reddit&logoColor=white" alt="Reddit"></a>
  <a href="https://www.instagram.com/stemdeck"><img src="https://img.shields.io/badge/Instagram-stemdeck-E4405F?style=flat-square&logo=instagram&logoColor=white" alt="Instagram"></a>
  <a href="https://x.com/StemDeckApp"><img src="https://img.shields.io/badge/X-StemDeckApp-000000?style=flat-square&logo=x&logoColor=white" alt="X"></a>
  <a href="https://stemdeck.app"><img src="https://img.shields.io/badge/Website-stemdeck.app-000000?style=flat-square&logo=safari&logoColor=white" alt="Website"></a>
</div>

</div>

<br>

Drop an MP3 or WAV, or paste a YouTube URL. StemDeck splits the audio into up to six stems (vocals, drums, bass, guitar, piano, other) and plays them back in a DAW-style multitrack mixer. Mute, solo, mix, zoom the waveform, loop a region, and download individual stems or a custom mix. Everything runs on your own machine.

> **What is this?** StemDeck is a stem separation tool, not a downloader. Its primary use case is processing audio files you already own — drag an MP3 or WAV onto the import bar and go. YouTube URL support is provided as a convenience for content you have the right to process. StemDeck does not store, cache, or redistribute any downloaded content. All processing happens locally on your machine and nothing leaves it.

> StemDeck is a free, open alternative to cloud stem-splitters like Moises and LALAL.AI. No account, no quota, no upload, no subscription. If you mainly want stems for personal study and prefer to keep things local and free, StemDeck should be enough. If you need the polish, the mobile app, or the extra musician tooling, the commercial products are a better fit.

![StemDeck screenshot](imgs/screenshot/stemdeck.png)

If you find StemDeck useful, consider [buying the maker a coffee](https://www.buymeacoffee.com/stemdeckapp); these donations are being used to random acts of kindness toward others 

---

## Features

**6-stem separation** via Demucs `htdemucs_6s`, with auto-detection of the best Torch device (CUDA on NVIDIA, MPS on Apple Silicon, CPU fallback).

**YouTube and local file import.** Paste a YouTube URL or drop an MP3 or WAV directly onto the import bar.

**DAW-style waveform editor** with min/max sample rendering across all stems, shared normalization, zoom in/out/Fit, loop drag on the ruler, gold playhead overlay, and stem-aligned lanes.

**Stem subset extraction.** Click stem chips to choose which stems to keep. Clicking from "all selected" snaps to "only this one"; subsequent clicks add or remove.

**"Original" backing track.** When you pick a subset, a 7th lane contains the complement (full song minus selected stems), perfect for A/B reference without doubling.

**Downloadable selected mix.** A single `mix.wav` of just your selected stems, summed via ffmpeg amix.

**Per-stem mixer** with volume fader, mute, solo, and "monitor" (solo-only) per stem. State syncs between the preview mixer and the stems sidebar.

**Live VU meters** per stem. Post-gain RMS via Web Audio analysers with peak hold and slow falloff.

**Song analysis** including BPM (librosa beat tracker), key, scale, and confidence (Albrecht-Shanahan profiles), integrated LUFS (BS.1770), and sample peak in dBFS.

**Cancellable jobs.** Cancel mid-pipeline and the runner terminates the active subprocess immediately, deletes the partia