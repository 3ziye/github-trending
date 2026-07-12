# claude-real-video

[![PyPI](https://img.shields.io/pypi/v/claude-real-video)](https://pypi.org/project/claude-real-video/) [![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://pypi.org/project/claude-real-video/) [![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE) [![HN front page](https://img.shields.io/badge/Hacker%20News-front%20page-orange)](https://news.ycombinator.com/item?id=48766005)

**Let Claude — or any LLM — actually watch a video.**

> **Naming:** crv is the short name for claude-real-video (the PyPI package). The paid add-on, **crv Pro**, is sold on Capafy under the listing name "llm-real-video Pro".

![demo](docs/demo.gif)

> Same 58-second clip: fixed 1 fps sampling = **58 frames**. crv keeps the **26 that actually differ** — and `--grid` packs them into **3 contact sheets**. Fewer tokens, nothing missed.

> **This free version lets your AI *see* the video.** [crv Pro](https://leoaido.com/crv-pro/) lets it *understand* it — how it was shot (cut rhythm, camera moves) plus a timestamped timeline of what frames can't show: gestures, expressions, voice pitch shifts, emotion, sound events. One-time founder price $19 — [get it on Capafy](https://capafy.ai/agent/llm-real-video-pro-let-any-llm-watch-videos/5451082151).

Most AI tools don't really *see* a video. Paste a YouTube link into ChatGPT and it
reads the **transcript**, not the picture. Claude won't take a video file at all.
Even Gemini, which *can* read video natively, has to send it up to Google and
samples frames at a **fixed interval** (1 fps by default), so fast cuts slip past.

`claude-real-video` does it differently, and **the processing runs locally**: point it at a URL or a
file, and it pulls the frames that *actually matter* (every scene change, not a
fixed quota), throws away the near-duplicates, transcribes the audio, and hands
you a clean folder any LLM can read. All the processing happens on your own machine — what gets sent anywhere is only the frames/text *you* choose to paste into an LLM afterwards.

```bash
crv "https://www.youtube.com/watch?v=..."
# → crv-out/frames/*.jpg  +  crv-out/transcript.txt (+ transcript.json with timestamps)  +  crv-out/MANIFEST.txt
```

Then drop the frames + `MANIFEST.txt` into Claude / ChatGPT / Gemini and ask away.

**No terminal needed** — run `crv-web` and a local page opens (Traditional Chinese / Simplified Chinese / English): paste a YouTube or Reels link or a file path, click Analyze, open the result viewer. Video analysis and output generation run on your machine — the source video never gets uploaded. (If you then paste the extracted frames or transcript into a cloud LLM, that data goes to that provider.)

Want to eyeball what the model will see first? Add `--viewer` — it writes a local `viewer.html` (video + keyframe grid + transcript) you can double-click open. No network, no extra installs.

**Slow-changing content** (animation tutorials, gradual morphs, slow pans): add `--adaptive` — frames are picked against their rolling neighbourhood instead of a fixed threshold, so a 2-3s squash-and-stretch that never spikes any single frame still gets captured.

**Text-heavy content** (lecture slides, screen recordings, talking-head explainers): add `--text-anchors` — extra frames are forced at subtitle-cue timestamps, so each spoken segment gets a matching visual even when the scene barely changes. Needs a sidecar `.srt`/`.vtt` or an embedded subtitle track — captions burned into the pixels can't be detected. At most one forced frame per second; scene detection is untouched.

Not doing LLM work? It also works as a **general-purpose video keyframe extractor** —
scene-change detection + dedup, no ML models to download.

**Using Claude Code?** Install it as a skill so Claude watches videos on its own
(the `skills/` folder lives in the repo, not in the pip package — clone it first):

```bash
pip install "claude-real-video[whisper]"
git clone https://github.com/HUANGCHIHHUNGLeo/claude-real-video.git
mkdir -p ~/.claude/skills && cp -r claude-real-video/skills/claude-real-video ~/.claude/skills/
```

Then just paste a video link into Claude Code and ask about it.

**New in 0.3.0** — tell it *why* you're watching, and keep what it finds:

```bash
crv "https://youtu.be/..." --why "find the pricing strategy" --kb ~/notes
```

`--why` makes the analysis focus on what you care about instead of a generic summary;
`--kb` saves the result as a dated note in your own notes folder, so it doesn't die in `crv-out`.

---

## Why not just sample frames?

Most "let an LLM watch a video" scripts (and Gemini's own pipeline) grab frames
at a **fixed interval** — e.g. one per second. That over-samples a static
screencast and under-samples a fast-cut reel. `claude-real-video` is smarter:

| | fixed-interval sampling | **claude-real-video** |
|---|---|---|
| Frame selection | every N seconds | **scene-change detection** + density floor |
| Repeated shots (A-B-A cuts) | sent 