[中文文档](README_zh.md)

# Gemini Lossless Watermark Remover - [banana.ovo.re](https://banana.ovo.re)

A high-performance, 100% client-side tool for removing Gemini AI watermarks. Built with pure JavaScript, it leverages a mathematically precise **Reverse Alpha Blending** algorithm rather than unpredictable AI inpainting.

<p align="center">
  <img src="https://count.getloli.com/@gemini-watermark-remover?name=gemini-watermark-remover&theme=minecraft&padding=7&offset=0&align=top&scale=1&pixelated=1&darkmode=auto" width="400">
</p>

## Features

- ✅ **100% Client-side** - No backend, no server-side processing. Your data stays in your browser.
- ✅ **Privacy-First** - Images are never uploaded to any server. Period.
- ✅ **Mathematical Precision** - Based on the Reverse Alpha Blending formula, not "hallucinating" AI models.
- ✅ **Auto-Detection** - Intelligent recognition of 48×48 or 96×96 watermark variants.
- ✅ **User Friendly** - Simple drag-and-drop interface with instant processing.
- ✅ **Cross-Platform** - Runs smoothly on all modern web browsers.

## Examples

<details open>
<summary>Click to Expand/Collapse Examples</summary>
　
<p>lossless diff example</p>
<p><img src="docs/lossless_diff.webp"></p>


<p>example images</p>

| Original Image | Watermark Removed |
| :---: | :----: |
| <img src="docs/1.webp" width="400"> | <img src="docs/unwatermarked_1.webp" width="400"> |
| <img src="docs/2.webp" width="400"> | <img src="docs/unwatermarked_2.webp" width="400"> |
| <img src="docs/3.webp" width="400"> | <img src="docs/unwatermarked_3.webp" width="400"> |
| <img src="docs/4.webp" width="400"> | <img src="docs/unwatermarked_4.webp" width="400"> |
| <img src="docs/5.webp" width="400"> | <img src="docs/unwatermarked_5.webp" width="400"> |

</details>

## ⚠️ Disclaimer

> [!WARNING]
>  **USE AT YOUR OWN RISK**
>
> This tool modifies image files. While it is designed to work reliably, unexpected results may occur due to:
> - Variations in Gemini's watermark implementation
> - Corrupted or unusual image formats
> - Edge cases not covered by testing
>
> The author assumes no responsibility for any data loss, image corruption, or unintended modifications. By using this tool, you acknowledge that you understand these risks.

> [!NOTE]
> **Note**: Disabling any fingerprint defender extensions (e.g., Canvas Fingerprint Defender) to avoid processing errors. https://github.com/journey-ad/gemini-watermark-remover/issues/3

## Usage

### Online Website

1. Open [banana.ovo.re](https://banana.ovo.re).
2. Drag and drop or click to select your Gemini-generated image.
3. The engine will automatically process and remove the watermark.
4. Download the cleaned image.

### Userscript for Gemini Conversation Pages

1. Install a userscript manager (e.g., Tampermonkey or Greasemonkey).
2. Open [gemini-watermark-remover.user.js](https://banana.ovo.re/userscript/gemini-watermark-remover.user.js).
3. The script will install automatically.
4. Navigate to Gemini conversation pages.
5. Click "Copy Image" or "Download Image" to remove the watermark.

## Development

```bash
# Install dependencies
pnpm install

# Development build
pnpm dev

# Production build
pnpm build

# Local preview
pnpm serve
```

## How it Works

### The Gemini Watermarking Process

Gemini applies watermarks using standard alpha compositing:

$$watermarked = \alpha \cdot logo + (1 - \alpha) \cdot original$$

Where:
- `watermarked`: The pixel value with the watermark.
- `α`: The Alpha channel value (0.0 - 1.0).
- `logo`: The watermark logo color value (White = 255).
- `original`: The raw, original pixel value we want to recover.

### The Reverse Solution

To remove the watermark, we solve for `original`:

$$original = \frac{watermarked - \alpha \cdot logo}{1 - \alpha}$$

By capturing the watermark on a known solid background, we reconstruct the exact Alpha map and apply the inverse formula to restore the original pixels with zero loss.

## Detection Rules

| Image Dimension Condition | Watermark Size | Right Margin | Bottom Margin |
| :--- | :--- | :--- | :--- |
| Width > 1024 **AND** Height > 1024 | 96×96 | 64px | 64px |
| Otherwise | 48×48 | 32px | 32px |

## Project Structure

```text
gemini-watermark-remover/
├── public/
│   ├── index.html         # Main page
│   └── terms.html         # Terms of Service page
├── src/
│   ├── core/
│   │   ├── alphaMap.js    # Alpha map calculation logic
│   │   ├── blendModes.js  # Implementation of Reverse Alpha Blending
│   │   └── watermarkEngine.js  # Main engine coordinator
│   ├── assets/
│   │   ├── bg_48.png      # Pre-captured 48×48 watermark map
│   │   └── bg_96.png      # Pre-captured 96×96 watermark map
│   ├── i18n/              # Internationalization language files
│   ├── userscript/        # Userscript for Gemini
│   ├── app.js             # Website application entry point
│   └── i18n.js            # Internationalization utilities
├── dist/                  # Build output directory
├── build.js               # Build s