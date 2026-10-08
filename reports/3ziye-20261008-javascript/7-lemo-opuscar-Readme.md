<div align="center">

# Lemo-Opuscar

**English** · [简体中文](README.zh-CN.md)

**<!--n-->43<!--/n--> film styles, each with a short film made entirely in code.**<br>
**<!--n-->43<!--/n--> 种影片风格，每种都配一支完全用代码做出来的短片。**

Pick a style, bring your own story, and let your coding agent direct the film.<br>
选一个风格，带上你自己的故事，让你的编程 agent 来当导演。

**🇨🇳 中文用户请看这里 → [简体中文说明 README.zh-CN.md](README.zh-CN.md)**

[**▶ Watch the gallery**](https://lemomo-ai.github.io/lemo-opuscar/)

<sub>Official repo: [github.com/lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) · by Lemomo ([@lemomo_ai](https://x.com/lemomo_ai))</sub>

**New:** Copperplate Engraving · Sci-fi Hologram HUD · Mid-century Cartoon · Silkscreen Travel Poster

</div>

## 🎬 Feature presentation: OPUSCAR 98

<div align="center">

<a href="https://lemomo-ai.github.io/lemo-opuscar/opuscar98/"><img src="docs/opuscar98.jpg" alt="OPUSCAR 98 — 98 Years of Best Picture" width="100%"></a>

**98 Years of Best Picture · 1927 – 2025 · 6:31**

One Clawd walks through all 98 Best Picture winners, each one redrawn in a style that fits the film.<br>
Every frame, every note and every cut was written in code by Claude Opus 5.5.

[**▶ Watch**](https://lemomo-ai.github.io/lemo-opuscar/opuscar98/) · [**Download 1080p**](https://github.com/lemomo-ai/lemo-opuscar/releases/download/films/opuscar98.mp4)

</div>

## 👋 About me

I'm **Lemomo** ([@lemomo-ai](https://github.com/lemomo-ai)). More about me on my profile.

> **Not an awesome list.** Every film here was made by me, with Claude Opus 5.5. The styles are tuned for Opus 5.5; other models may not reproduce them.

![All styles](docs/cover.jpg)

Every film was directed, drawn, scored and mixed by an AI agent writing code: canvas and WebGL pages rendered frame by frame, original music from free sample libraries, text-to-speech narration. No video generation, no stock footage.

## How to use

Two ways in; the skill is the easiest.

### Option 1: install the skill (recommended)

In your terminal:

```sh
claude plugin marketplace add lemomo-ai/lemo-opuscar
claude plugin install lemo-opuscar@lemolab
```

Then use it from any folder. On first use it downloads the guides, tools and style prompts to `~/lemo-opuscar`, shared by all your films. Each film's project, from source to finished video, goes in the folder you started from. For other agents, copy [`plugin/skills/lemo-opuscar/`](plugin/skills/lemo-opuscar/) into their skills folder.

### Option 2: clone the repo

```sh
git clone https://github.com/lemomo-ai/lemo-opuscar.git
cd lemo-opuscar
claude
```

Films go into `films/<name>/` inside the repo.

### Then just say what you want

> Make a 45-second film in the **watercolor** style about the coffee farm my family runs. Warm female narrator.

Name the style in English or Chinese; the [style index](styles/README.md) lists them all.

It asks you once, up front: anything it can't decide about your topic, whether you have your own **voice, music or other material**, and whether you want to see a **storyboard** first. Say yes and it stops once to show you the key shots in the real style; otherwise it goes straight to the finished film.

The agent reads three guides and works like a small studio:

| File | What it gives the agent |
|---|---|
| [`DIRECTOR.md`](DIRECTOR.md) | how to direct: story, sound, rhythm, camera, performance, self-checks |
| [`TECHNIQUE.md`](TECHNIQUE.md) | how to build: frame-by-frame rendering, voice, music, mixing |
| `styles/<style>/STYLE.md` | what the style looks and sounds like; the story is yours |

### Before you start

- A film takes an agent about 30–60 minutes and a fair amount of tokens.
- You need Node 20+, ffmpeg and Python 3.11+ (or [uv](https://docs.astral.sh/uv/)); the agent installs the rest.
- Default output 1920×1080, 24 fps; other sizes on request.

Update: `claude plugin marketplace update lemolab && claude plugin update lemo-opuscar@lemolab`, then restart Claude Code (the library in `~/lemo-opuscar` updates itself on the next film); uninstall with `claude plugin uninstall lemo-opuscar@lemolab` and delete `~/lemo-opuscar`. If a step stays stuck, [open an issue](https://github.com/lemomo-ai/lemo-opuscar/issues).

## The styles

Click a frame for its `STYLE.md`.

<!-- styles:start -->

### Hand-drawn & Painting

<table>
<tr>
<td width="33%" valign="top"><a href="styles/crayon-book/STYLE.md"><img src="docs/frames/crayon-book.jpg" alt="Crayon Picture Book"></a><br><b>Crayon Picture Book</b><br><i>The Moon Can&#x27;t Sleep</i><br><sub>The moon can&#x27;t sleep, so a little girl climbs onto the roof to sing it a lullaby.</sub></td>
<td width="33%" valign="top"><a href="styles/watercolor/STYLE.md"><img src="docs/frames/watercolor.jpg" alt="Watercolor Brush"></a><br><b>Watercolor Brush</b><br><i>Follow the Rain</i><br><sub>Follow the rain from Australia&#x27;s red desert heart to its green coast in one unbroken painted walk.</sub></td>
<td width="33%" valign="top"><a href="styles/ink-wash/STYLE.md"><i