<div align="center">

# rea-video

Reverse-engineer any video.

Talking-head, tabletop, AI video, 3D, motion graphics, mixed edits: give it any of them,<br>
and it tells you shot by shot how the visuals, styled text, editing and audio were made, then gives you a plan to make one yourself.

[中文](i18n/README_zh.md) | English | [Русский](i18n/README_ru.md) | [日本語](i18n/README_ja.md) | [한국어](i18n/README_ko.md) | [Español](i18n/README_es.md) | [Português](i18n/README_pt.md) | [Français](i18n/README_fr.md) | [Deutsch](i18n/README_de.md)

[![Stars](https://img.shields.io/github/stars/JuneYaooo/rea-video?style=flat)](https://github.com/JuneYaooo/rea-video/stargazers)
![Python](https://img.shields.io/badge/python-%E2%89%A53.10-blue)
![Agent](https://img.shields.io/badge/runs%20in-Claude%20Code%20%7C%20Codex-8A2BE2)

<img src="docs/cases/demo.gif" width="440" alt="Left: TikTok original shot on a phone; right: someone's AI remake with a different product">

Left: a TikTok ad shot on a phone. Right: someone's AI remake with a different product swapped in.<br>
rea-video's verdict: the left is all live footage, one set and two camera positions; the right is all AI-generated, and its 8 shots can be produced in 3 generations.

</div>

> Reports come out in the language you ask in (Chinese or English; your agent passes `--lang`). The detailed docs are in Chinese for now; your agent reads them and answers in your language. The six example reports below are in English, so you can see what a report looks like without installing anything.

## What it can break down

| Video type | Examples | What you get |
|---|---|---|
| Live footage | Talking-head, tabletop, handheld product demo, vlog, store visit | Setups and camera positions, framing, camera moves, lighting (12 setups with gear lists), color grade |
| AI video | Text/image-to-video, AI short drama, AI music video | Evidence, a reverse-engineered prompt per shot, how to batch into generations and which model to use |
| Avatar | A portrait driven by audio, lip-sync | Which shots are avatar shots, what portrait and audio you need |
| 3D / animation | Blender / C4D explainers, product animation, 2D animation, stop-motion | Whether to generate with a video model or render from 3D code |
| Code / template | Kinetic type, UI demos, charts, slide-style cards | Text, layout and motion timing, ready to rebuild as a Remotion project |
| Screen recording | Software tutorials, web demos | Which parts are real material you'll need to record yourself |
| Mixed / edits | AI characters + code UI + real screen capture; live footage with AI edits | Each shot judged separately, then reassembled on the original timeline |

Besides how the picture was made, every video also gets:

- Captions and styled text: start and end of each line (exports to SRT / ASS), plus color, outline and how the text comes in
- Stickers, emoji, picture-in-picture: where they sit and how long they stay
- Editing: where the cuts are, how fast, whether they hit the beat
- Audio: human or AI voice, AI or library music and its BPM, where each sound effect lands
- Material you'll supply yourself: screen recordings, screenshots, product photos

## Quick start

rea-video is built for AI agents. In Claude Code, Codex or any agent that can run commands, say:

```text
Install https://github.com/JuneYaooo/rea-video, then break down this video: /path/to/video.mp4
```

The agent installs the CLI, learns the workflow and runs the whole thing. You need ffmpeg and Python 3.10+.

<details><summary>Install by hand</summary>

```bash
brew install ffmpeg            # or: sudo apt install ffmpeg
git clone https://github.com/JuneYaooo/rea-video && cd rea-video
bash scripts/install_skill.sh  # installs the CLI (pip, or pipx / a local .venv if pip is blocked) and links the skill into ~/.claude, ~/.codex, ~/.agents
rea-video --help
```

</details>

You get:

- a one-line summary, e.g. "41% AI video + 59% code UI, 8 s of real screen recording, library music at 122 BPM"
- a remake plan, split into what to film, what to generate and what to code
- a full `report.html` with per-shot frames, evidence, prompts, camera and lighting notes, and the audio breakdown

Add a video-capable model — Gemini or Doubao both work: give the agent the endpoint and key. It makes live/AI/3D calls more accurate and writes a reverse-engineered prompt for every shot. Without one it still works; if your agent can see images, it will check the uncertain shots itself.

## Examples

The sample videos in `docs/cases/videos/` are re-compressed to keep the repo small, which strips the TikTok / Douyin platform tags. Running them yourself gives different results from the reports below, especially without a vision model. Use the original platform download to reproduce.

<table>
<tr>
<td width="50%" valign="top">
<a href="docs/cases.md#2-混合片ai-人物对话--代码界面--真实录屏"><img src="docs/cases/dual_role/thumb.jpg"></a><br>
<b>Mixed-media clip</b> · 19 s · 10 shots<br>
AI characters talking +