# ffmpeg webCLI

[![GitHub stars](https://img.shields.io/github/stars/tejaswigowda/ffmpeg-webCLI?style=social)](https://github.com/tejaswigowda/ffmpeg-webCLI/stargazers)

A browser-based video editor powered by [ffmpeg.wasm](https://github.com/ffmpegwasm/ffmpeg.wasm). <b><ins>No uploads, no servers -- all processing happens locally</ins></b> in your browser using WebAssembly.

▶ **Live app:** https://tejaswigowda.com/ffmpeg-webCLI/

---

## Key Features

<img src='demos/features.png'/>


✓ **No Server Uploads** : All video processing happens entirely on your device

✓ **32+ Video Operations** : GIF creation, format conversion, compression, trimming, effects, filters, auto-captioning, and more

✓ **Batch Processing** : Process multiple videos at once with the same operation - or an entire **operation chain** - applied to every file; real-time progress, per-file preview, individual downloads, ZIP-all, and graceful fallback

✓ **Offline-First PWA** : Works completely offline after first use; install as a native app

✓ **Screen Wake Lock** : Screen stays active during video processing on any device

✓ **Live Previews** : See output size estimates and live settings adjustments

✓ **Multi-Format Support** : MP4, WebM, MKV, MOV, AVI, GIF, MP3, AAC, WAV, OGG, FLAC, JPG, PNG

✓ **Advanced Features** : Raw ffmpeg command access, subtitle embedding, concatenation, picture-in-picture, audio mixing

✓ **Fast & Responsive** : Uses Web Workers for background processing

✓ **Privacy First** : Zero data collection; works with your files locally

---

## What It Replaces

| Tool | What you replace |
|---|---|
| CloudConvert | Format conversion, compression, audio extraction |
| Kapwing | Trim, crop, speed, reverse, fade, filters |
| Clideo | Trim, compress, merge, mute, loop |
| Ezgif | GIF maker, reverse, resize, crop, optimize |
| Online-convert.com | Format conversion across video/audio |
| MP3cut / Audiotrimmer | Audio extraction and trimming |
| Metadata2go | Strip metadata |
| Subtitle Horse | Embed subtitles |
| Kapwing (side-by-side) | Side by side, picture-in-picture |
| Rev / Scribd | Auto-captioning, transcript editing |
| Loudnorm tools | Audio normalization |

**The difference that matters:** every one of those tools uploads your file to a
server. Some are free with ads, some charge -- but all of them *see your file*, and
all are subject to data breaches, subpoenas, and privacy-policy changes.

ffmpeg-webCLI covers the common tasks of all of them, for free, with files that
**never leave your device**.


---

## Use Cases

### ⛓ Operation Chaining (Stack Mode)
Stack several compatible operations and run them in a **single pass**. Switch the Operations panel to **Stack (chain)** mode, configure an op, and click **Add to Stack** to queue it. The queue is an ordered, reorderable list - move items up/down or remove them - and a live **composed command preview** shows the exact `ffmpeg` invocation before you run it.

All stacked operations are merged into one filter chain (`-vf "a,b,c"` / `-af "x,y"`) and encoded **only once**, so quality loss from repeated re-encoding is avoided. Any active trim is applied first as input seeking, then the chain runs, then the single encode targets your chosen output format. For example, crop → grayscale → convert-to-MP4 becomes:

```
ffmpeg -i input.mp4 -vf "crop=1280:720:0:0,eq=brightness=0:contrast=1:saturation=0" -c:v libx264 -preset fast -c:a aac output.mp4
```

**Chainable:** Crop, Resize, Rotate/Flip, Adjust (brightness/contrast/saturation), Grayscale, Fade, Denoise, Sharpen/Blur, Speed, Pad/Letterbox and Volume - every single-input, frame-wise video/audio filter.

**Not chainable** (use Single mode): multi-input operations (Concatenate, Side by Side, Picture in Picture, Mix Audio, Embed Subtitles, Logo Overlay) and whole-file or different-output operations (GIF, Thumbnail, Boomerang, Media Info). These are disabled in Stack mode with an inline explanation.

**Chaining + batch together:** Stack mode and batch mode combine - enable **Batch**, queue several files, switch to **Stack (chain)**, build your chain once, and click **Process Stack** to apply the *entire* chain to *every* queued file. Each file is composed against its own dimensions/duration (so crop, pad, and fade resolve per file) and encoded in a single pass, with results shown in the batch outputs panel.

### ▶ Batch Processing
Process multiple video files with the same operation in a single session. Click the **Batch** toggle in the Input Video card to enable batch mode, then drop or select multiple files. Each file is queued with a status indicator:
- ⧖ **Pending** : queued, waiting to process
- ▶ **Processing** : currently encoding
- ✓ **Done** : completed successfully
- ✗ **Error** : encountered an issue

When you click **Process Queue**, ffmpeg runs through each file sequentially. The log shows real-time progress: `[X/total] Processing: filename`. Completed files appear in the **Batch Outputs** panel of the Outp