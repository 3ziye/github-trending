# franken_ocr

<div align="center">
  <img src="franken_ocr_illustration.webp" alt="franken_ocr - Pure-Rust CPU-only OCR for Baidu Unlimited-OCR">
</div>

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![source tag: v0.6.0](https://img.shields.io/badge/source_tag-v0.6.0-blue.svg)](https://github.com/Dicklesworthstone/franken_ocr/tree/v0.6.0)
[![binary release: v0.6.0](https://img.shields.io/badge/binary_release-v0.6.0-blue.svg)](https://github.com/Dicklesworthstone/franken_ocr/releases/tag/v0.6.0)
[![status: working](https://img.shields.io/badge/status-working-success.svg)](#quick-example)
[![Rust Edition](https://img.shields.io/badge/Rust-2024_Edition-orange.svg)](https://doc.rust-lang.org/edition-guide/rust-2024/)
[![toolchain: nightly](https://img.shields.io/badge/toolchain-nightly-purple.svg)](./rust-toolchain.toml)
[![unsafe: forbidden*](https://img.shields.io/badge/unsafe-forbidden*-success.svg)](https://github.com/rust-secure-code/safety-dance/)
[![default model: Baidu Unlimited-OCR](https://img.shields.io/badge/default_model-Baidu_Unlimited--OCR-teal.svg)](https://huggingface.co/baidu/Unlimited-OCR)
[![release readiness: 13/13 green](https://img.shields.io/badge/release_readiness-13%2F13_green-success.svg)](#conformance-and-release-evidence)

</div>

**A pure-Rust, memory-safe, CPU-only OCR engine for a small family of hand-ported vision-language models.** Baidu Unlimited-OCR is the fast default for document OCR, GOT-OCR2 handles specialized structured formats, SmolVLM2 handles image description and VQA, OneChart extracts chart data, and Polyphonic-TrOMR turns full scanned sheet-music pages or staff crops into MusicXML through `--task music`. All five ready models are available through `focr pull`; TrOMR now publishes both the 61 MB int8 default artifact and an 86 MB f32 reference artifact. They run through model-specific Rust kernels and need no general ML framework, Python, CUDA, FFI at inference, or GPU. The single portable binary parses document images and PDFs into Markdown, MusicXML, structured JSON, or versioned NDJSON; the current release assets are about 13 to 17 MB depending on platform.

<div align="center">
<h3>Quick Install</h3>

```bash
curl -fsSL https://raw.githubusercontent.com/Dicklesworthstone/franken_ocr/main/install.sh | bash
```

</div>

The installer detects your platform, resolves the latest published GitHub binary release (currently `v0.6.0`), verifies the downloaded asset by SHA256, and puts `focr` on your PATH. Then `focr pull` fetches the weights once and every later inference run is offline.

### Current Release

`v0.6.0` is the first release cut after the full gauntlet closed: the source tag and binary assets were published together on 2026-07-08, the release-readiness gate is 13/13 green, and the Unlimited-OCR performance ledger contains paired end-to-end rows where the native int8 path beats the pinned Hugging Face/PyTorch bf16 CPU reference at matched thread counts. The release ships raw executables for macOS Apple Silicon, macOS Intel, Linux x86-64, Linux ARM64, and Windows x86-64, each with a SHA256 sidecar.

---

## TL;DR

**The problem.** Baidu Unlimited-OCR is a strong document-parsing model: Markdown, tables, LaTeX, reading order, many pages in one pass. The official stack is Python plus CUDA. Most machines that need OCR (laptops, CI runners, agent hosts, edge boxes) have no usable GPU, and a Python plus CUDA dependency is heavy to ship and awkward to embed.

**The solution.** `franken_ocr` is a library plus a single-binary CLI (`focr`) that runs the ready model set on CPU with nothing but a Rust binary. It transforms bf16 checkpoints into custom `.focrq` int8 artifacts and runs them through kernels written for each model's exact shapes. On a real Unlimited-OCR page measured against the Baidu reference, the end-to-end character-error-rate is **0.0094**; the decode matched the reference to within a single token, and on one token it beat the reference. That is a measured result on the 6.67 GB model, not a target.

### Why `focr`?

| Feature | What it does |
|---|---|
| **One portable binary** | No Python, no CUDA, no FFI at inference, no GPU. Current release assets are about 13 to 17 MB; portable to hosts where `ort`/CUDA cannot build. |
| **Works offline** | `focr pull` fetches and verifies the weights once into `~/.cache/franken_ocr/models`; inference never touches the network. The default loader memory-maps `.focrq` and safetensors artifacts, so multi-GB weights page in lazily and share the OS page cache across runs. |
| **Embeddable Rust API** | `OcrEngine` exposes synchronous, blocking calls for Markdown, structured layout, figure extraction, in-memory images, and load-once batches. |
| **Native PDFs and figures** | Scanned PDFs are rasterized in process with pure Rust; page `/Rotate` and image-placement rotations are honored, `--pages` selects exact PDF pages, `--split-spreads` can split two-page book 