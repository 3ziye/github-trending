<p align="right"><b>English</b> · <a href="README.zh.md">简体中文</a></p>

# 🎬 Vox Director

**Turn one topic into a finished Vox-style paper-collage explainer / ad video — script, collage keyframes, motion, voice-over, music and captions, all automated.**

An **agent skill** that runs end to end on the [Atlas Cloud](https://www.atlascloud.ai/?utm_source=github&utm_campaign=vox_director) API + local `ffmpeg`, usable by any coding agent (Claude Code, Codex, etc.). You give it a one-line topic; it gives you an `mp4`.

![License: MIT](https://img.shields.io/badge/License-MIT-black.svg) ![Powered by Atlas Cloud](https://img.shields.io/badge/powered%20by-Atlas%20Cloud-ff5a1f.svg) ![Agent Skill](https://img.shields.io/badge/Agent-Skill-d97757.svg)

<div align="center">

https://github.com/user-attachments/assets/ed08d230-7bcb-4b48-a17d-23c079208f9f

<b>▶ "The evolution of Chinese civilization" · 30s</b>

</div>

<table>
  <tr>
    <td width="25%"><a href="https://github.com/user-attachments/assets/216cd62f-6314-456c-94cf-1090b8559a22"><img src="assets/thumbs/football.jpg" width="100%" alt="How football conquered the world"></a></td>
    <td width="25%"><a href="https://github.com/user-attachments/assets/561788b1-5615-4828-b3f8-b24ae5ad7bcd"><img src="assets/thumbs/mexican.jpg" width="100%" alt="Mexican street food"></a></td>
    <td width="25%"><a href="https://github.com/user-attachments/assets/f69f072f-f50a-41ba-9e66-7ed0aae4ddc0"><img src="assets/thumbs/money.jpg" width="100%" alt="A brief history of money"></a></td>
    <td width="25%"><a href="https://github.com/user-attachments/assets/b9ff526f-577f-4acb-aafe-a2519a9b7c1c"><img src="assets/thumbs/silicon-valley.jpg" width="100%" alt="A brief history of Silicon Valley"></a></td>
  </tr>
  <tr>
    <td align="center"><sub>Football history · 60s</sub></td>
    <td align="center"><sub>Mexican street food · 60s</sub></td>
    <td align="center"><sub>A brief history of money · 60s</sub></td>
    <td align="center"><sub>Silicon Valley history · 60s</sub></td>
  </tr>
</table>

<p align="center"><sub><em>▶ more films — click any thumbnail to play</em></sub></p>

---

## What it is

The look is the modern editorial **paper-collage** popularized by Vox explainers: hand-cut paper cut-outs, torn edges, tape, halftone dots, newspaper clippings, bold flat color per beat, big cut-out headlines — brought to life with motion, a narrator, music and captions.

## How it works

One topic flows through one script per stage, all driven by a single `beats.json` per project:

```
topic
  │
  ├─ 1. beat map        pick a narrative arc → write beats.json      ◀── GATE 1: you approve the beat map
  ├─ 2. style bake-off  render the same beat in 3–4 themes           ◀── GATE 2: you pick the look by eye
  ├─ 3. keyframes       one collage poster per beat  (nano-banana-2)
  ├─ 4. motion          animate each poster          (gemini-omni-flash i2v)
  ├─ 5. voice + music   one narrator (xai/tts) + BGM (minimax/music)
  ├─ 6. assemble        ffmpeg: concat, duck music under VO, burn captions + watermark
  └─ final.mp4
```

That flow is **B-roll** — a topic in, everything generated. Two more input modalities reuse the same engine:

- **A-roll — you already have a talking-head video.** It is ASR-segmented into beats and re-styled into the collage look, keeping the real face, lip-sync and gestures frame-for-frame (`gemini-omni-flash/video-edit`, auto-retrying on `seedance-2.0/reference-to-video`).
- **C-roll — you have one still photo** (a selfie, a product shot). The subject is cut out as a photographic sticker — never redrawn — and each beat's poster is generated around it (`nano-banana-2/edit`). The narration can be cloned into the subject's own voice.

Two ideas make or break the result, and the skill is built around both:

1. **The look is born in the image step.** Each beat is a finished collage *poster*. All the collage DNA (torn paper, cut-outs, halftone, headline text) lives in that image — if the poster isn't a rich collage, nothing downstream saves it.
2. **The motion is added after.** By default an AI video model animates the whole poster (the "living poster" path). For dramatic *piece-by-piece* assembly, an optional local keyframe engine cuts the poster into parts and drives them frame-by-frame (no content filters, pixel-exact — great for real people).

Two human decision gates keep you in control (approve the beat map; pick the style); everything else is automated.

## Models (verified on Atlas Cloud)

| Job | Model |
|---|---|
| Keyframe / collage poster | `google/nano-banana-2/text-to-image` |
| Animate (non-real content) | `google/gemini-omni-flash/image-to-video` |
| Animate (**real people / brands**) | `kwaivgi/kling-video-o3-pro/image-to-video` |
| Re-style a talking-head (A-roll) | `google/gemini-omni-flash/video-edit` |
| Anchor a photo in the collage (C-roll) | `google/nano-banana-2/edit` |
| Narration | `xai/tts-v1` |
| Narration in a real person's voice | `bytedance/seed-au