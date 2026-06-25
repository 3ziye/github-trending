# ffmpeg webCLI

[![GitHub stars](https://img.shields.io/github/stars/tejaswigowda/ffmpeg-webCLI?style=social)](https://github.com/tejaswigowda/ffmpeg-webCLI/stargazers)

A browser-based video editor powered by [ffmpeg.wasm](https://github.com/ffmpegwasm/ffmpeg.wasm). <b><ins>No uploads, no servers -- all processing happens locally</ins></b> in your browser using WebAssembly.

▶ **Live app:** https://tejaswigowda.com/ffmpeg-webCLI/

---

## Key Features

<img src='demos/features.png'/>


✓ **No Server Uploads** : All video processing happens entirely on your device

✓ **30+ Video Operations** : GIF creation, format conversion, compression, trimming, effects, filters, auto-captioning, and more

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

### ▶ GIF Maker
Convert any video clip into an animated GIF. Set the frame rate and output width; height scales automatically to preserve the aspect ratio. Uses a two-pass palette generation for the best possible color quality.

<img src='demos/makegif.gif'>

### ↻ Video Format Converter
Re-encode a video to a different container and codec:
- **MP4** : H.264 + AAC, widest compatibility
- **WebM** : VP9 + Opus, open format optimised for the web (~45% smaller than MP4 at similar quality)
- **MKV / MOV** : H.264 + AAC in alternative containers
- **AVI** : legacy compatibility

### ⊟ Video Compression
Reduce file size without changing the resolution. Dial in the quality with a **CRF slider** (18 = near-lossless → 51 = maximum compression) and pick an encoding **preset** (ultrafast → veryslow) to trade encoding speed for compression efficiency. A live size estimate updates as you adjust the settings.

### ▤ Video Trimming
Set a start and end point with the timeline sliders before running any operation. Trimming is applied on top of every other operation, so you can, for example, extract a short clip, compress it, and convert it to GIF all at once.

### ⊞ Resize & Compress
Change the output dimensions and compress in one pass. Width and height are auto-filled from the source video; edit either value or leave it blank to let ffmpeg maintain the aspect ratio. Combines a `scale` filter with CRF-based H.264 encoding.

### ♪ Audio Extraction
Pull the audio track out of any video into a standalone audio file:
- **MP3** : universal playback
- **AAC** : efficient lossy, great for mobile
- **WAV** : uncompressed PCM
- **OGG Vorbis** : open lossy format
- **FLAC** : lossless compression

### ⊘ Mute Video
Strip the audio stream entirely. Output is the original video with no audio track -- useful for silent loops, social media clips, or before replacing the audio elsewhere.

### ▶ Speed Change
Speed up or slow down playback (0.25× – 4×). Both the video PTS and the `atempo` audio filter chain are adjusted so audio pitch and sync are preserved. Chains multiple `atempo` stages automatically when the multiplier is outside the 0.5–2.0 range that a single filter accepts.

### ↻ Rotate / Flip
Correct orientation or create mirror effects without re-uploading. Options: 90° clockwise, 90° counter-clockwise, 180°, flip horizontal, flip vertical, or flip both axes.

<img src='demos/invert.gif'>

### ▤ Crop
Trim the frame to