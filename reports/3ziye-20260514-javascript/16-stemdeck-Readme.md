<div align="center">

<img src="imgs/stemdeck-svg-assets/stemdeck-logo-stacked.svg" alt="StemDeck" width="515" />

**Free, local stem separation. No account. No upload. No subscription.**

<div align="center">
  <a href="https://github.com/thcp/stemdeck/stargazers"><img src="https://img.shields.io/github/stars/thcp/stemdeck?style=flat-square" alt="GitHub Stars"></a>
  <a href="https://github.com/thcp/stemdeck/releases"><img src="https://img.shields.io/github/downloads/thcp/stemdeck/total?style=flat-square&color=52c65f" alt="Total Downloads"></a>
  <a href="https://github.com/thcp/stemdeck/releases/latest"><img src="https://img.shields.io/github/v/release/thcp/stemdeck?style=flat-square" alt="Latest Release"></a>
  <a href="https://github.com/thcp/stemdeck/blob/main/LICENSE"><img src="https://img.shields.io/github/license/thcp/stemdeck?style=flat-square" alt="License"></a>
  <img src="https://img.shields.io/badge/CI-Woodpecker-4D9DE0?style=flat-square&logo=woodpecker-ci&logoColor=white" alt="CI: Woodpecker">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-0078D6?style=flat-square&logo=windows" alt="Platform">
  <img src="https://img.shields.io/badge/Powered_by-Demucs-FF6B35?style=flat-square" alt="Powered by Demucs">
</div>

</div>

<br>

Drop an MP3 or WAV, or paste a YouTube URL. StemDeck splits the audio into up to six stems (vocals, drums, bass, guitar, piano, other) and plays them back in a DAW-style multitrack mixer. Mute, solo, mix, zoom the waveform, loop a region, and download individual stems or a custom mix. Everything runs on your own machine.

> **What is this?** StemDeck is a stem separation tool, not a downloader. Its primary use case is processing audio files you already own — drag an MP3 or WAV onto the import bar and go. YouTube URL support is provided as a convenience for content you have the right to process. StemDeck does not store, cache, or redistribute any downloaded content. All processing happens locally on your machine and nothing leaves it.

> StemDeck is a free, open alternative to cloud stem-splitters like Moises and LALAL.AI. No account, no quota, no upload, no subscription. If you mainly want stems for personal study and prefer to keep things local and free, StemDeck should be enough. If you need the polish, the mobile app, or the extra musician tooling, the commercial products are a better fit.

![StemDeck screenshot](imgs/screenshot/stemdeck.png)

If you find StemDeck useful, consider [buying the maker a coffee](https://buymeacoffee.com/tha.les); these donations are being used to random acts of kindness toward others 

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

**Cancellable jobs.** Cancel mid-pipeline and the runner terminates the active subprocess immediately, deletes the partial job dir, and returns to ready.

**Library panel** with folder-based track organisation, drag-and-drop, search, and trash.

---

## Honest Comparison

StemDeck is not trying to compete with commercial stem-separation products. It covers the core use case well and stops there. This table exists so you can make an informed choice rather than discover the gaps after the fact.

| | StemDeck | Moises / LALAL.AI / similar |
|---|---|---|
| **Price** | Free, forever | Freemium; credits or subscription required for regular use |
| **Hosting** | Runs entirely on your machine | Cloud; audio must be uploaded to their servers |
| **Account / login** | None | Required |
| **Internet required** | Only for YouTube download and first model fetch (~170 MB, cached after) | Always; no offline use |
| **Privacy** | Audio never leaves your machine | Audio is uploaded and processed on third-party servers |
| **Data retention** | You co