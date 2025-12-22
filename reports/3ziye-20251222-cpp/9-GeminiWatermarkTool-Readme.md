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

This will **remove the watermark in-place**, overwriting the original file.

> ⚠️ **Warning**: Simple mode overwrites the original file permanently. **Always back up important images before processing.**

### Standard Mode

For more control, use the `-i` (input) and `-o` (output) options:

```bash
# Single file
GeminiWatermarkTool -i input.jpg -o output.jpg

# With explicit --remove flag (optional)
GeminiWatermarkTool -i input.jpg -o output.jpg --remove
```

## Batch Processing (Directory Mode)

Process all images in a directory:

```bash
GeminiWatermarkTool -i ./watermarked_images/ -o ./clean_images/
```

- Input: directory
- Output: directory
- Supported formats: `.jpg`, `.jpeg`, `.png`, `.webp`, `.bmp`

## Command Line Options

| Option | Short | Description |
|--------|-------|-------------|
| `--input <path>` | `-i` | Input image file or directory |
| `--output <path>` | `-o` | Output image file or directory |
| `--remove` | `-r` | Remove watermark (default behavior) |
| `--force-small` | | Force 48×48 watermark size |
| `--force-large` | | Force 96×96 watermark size |
| `--verbose` | `-v` | Enable verbose output |
| `--quiet` | `-q` | Suppress all output except errors |
| `--banner` | `-b` | Show full ASCII banner |
| `--version` | `-V` | Show version information |
| `--help` | `-h` | Show help message |

## Watermark Size Detection

The tool automatically detects the appropriate watermark size based on image dimensions:

| Image Size | Watermark | Position |
|------------|-----------|----------|
| W ≤ 1024 **or** H ≤ 1024 | 48×48 | Bottom-right, 32px margin |
| W > 1024 **and** H > 10