# Gemini Watermark Tool

Gemini Watermark Tool is a lightweight, standalone command-line utility that removes Gemini Nano Banana / Pro watermarks from images using **mathematically accurate reverse alpha blending**.

- **Fast & offline**: single executable, **zero dependencies**
- **Flexible workflows**: in-place editing, explicit input/output, and **batch directory** processing
- **Cross-platform**: Windows / Linux / macOS / Android
- **Auto detection**: detects 48×48 vs 96×96 watermark size automatically

<!-- CLI Preview -->
![Preview](artworks/preview.png)

## Features

- **Batch Processing** - Process entire directories at once
- **One-Click Removal** - Simply drag & drop an image onto the executable
- **In-Place Editing** - Process files directly without specifying output
- **Deterministic (Not Inpainting)** - Restores pixels via reverse alpha blending (no guessing)
- **Cross-Platform** - Windows, Linux, macOS, and Android
- **Zero Dependencies** - Single standalone executable, no installation required
- **Auto Size Detection** - Automatically detects 48×48 or 96×96 watermark size
- **Mathematically Accurate** - Precise restoration using reverse alpha blending

## Demo

![Comparison](artworks/demo.gif)

## Side by Side Comparison

![Comparison](artworks/comparison.png)
Best for: **slides, documents, UI screenshots, diagrams, logos**.

**Focus on the bottom example (text-heavy slide).**  
Generative inpainting often breaks text: warped edges, wrong spacing, invented strokes.  
GeminiWatermarkTool reverses the blending equation to recover pixels, keeping text crisp.

---

## ⚠️ About SynthID (Invisible Watermark)

> **Important**: This tool removes **visible watermarks only**. It does NOT remove SynthID.

### What is SynthID?

SynthID is Google DeepMind's **invisible watermarking** technology embedded in AI-generated images. Unlike visible watermarks:

- **Invisible** to human eyes
- **Integrated** during generation (not added afterward)  
- **Extremely robust** against common image manipulations

### Why Can't SynthID Be Removed?

Our extensive research revealed a fundamental truth:

> **SynthID is not a watermark added to an image — it IS the image.**

SynthID operates as a **Statistical Bias** during generation. Every pixel choice is subtly influenced by Google's private key using **Tournament Sampling**. The watermark and visual content are **inseparably bound**.

```
Visible Watermark:  Image + Overlay = Result     ✓ Removable (this tool)
SynthID:            Biased Generation = Image    ✗ Cannot separate
```

### Potential Removal Approaches

| Approach | Trade-off | Feasibility |
|----------|-----------|-------------|
| **Extreme Quantization** (binarization) | Image becomes unusable skeleton | ✓ Works |
| **AI Repaint** (Stable Diffusion, etc.) | Style changes significantly | ✓ Works |
| **White-box Adversarial Attack** | Requires detector model | ✗ Not available |

**Conclusion**: Removing SynthID while preserving image quality is **currently not feasible**.

📄 **[Full SynthID Research Report →](report/synthid_research.md)**
- [SynthID Image Watermark Research Report](https://allenkuo.medium.com/synthid-image-watermark-research-report-9b864b19f9cf)

---

## Download

Download the latest release from the [Releases](https://github.com/allenk/GeminiWatermarkTool/releases) page.

| Platform | File | Architecture |
|----------|------|--------------|
| Windows | `GeminiWatermarkTool-Windows-x64.exe` | x64 |
| Linux | `GeminiWatermarkTool-Linux-x64` | x64 |
| macOS | `GeminiWatermarkTool-macOS-Universal` | Intel + Apple Silicon |
| Android | `GeminiWatermarkTool-Android-arm64` | ARM64 |

## ⚠️ Disclaimer

> **USE AT YOUR OWN RISK**
>
> This tool modifies image files. While it is designed to work reliably, unexpected results may occur due to:
> - Variations in Gemini's watermark implementation
> - Corrupted or unusual image formats
> - Edge cases not covered by testing
>
> **Always back up your original images before processing.**
>
> The author assumes no responsibility for any data loss, image corruption, or unintended modifications. By using this tool, you acknowledge that you understand these risks.

## Quick Start

<img src="artworks/app_ico.png" alt="App Icon" width="256" height="256">

### Simplest Usage (Drag & Drop) - Windows

1. Download `GeminiWatermarkTool-Windows-x64.exe`
2. Drag an image file onto the executable
3. Done! The watermark is removed in-place

### Command Line

```bash
# Simple mode - edit file in-place
GeminiWatermarkTool watermarked.jpg

# Specify output file
GeminiWatermarkTool -i watermarked.jpg -o clean.jpg

# Batch processing
GeminiWatermarkTool -i ./input_folder/ -o ./output_folder/
```

## Usage

### Simple Mode (Recommended)

The easiest way to use this tool - just provide a single image path:

```bash
GeminiWatermarkTool image.jpg
```
