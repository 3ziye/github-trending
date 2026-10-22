<div align="center">

# Lemo-Opuscar

**<!--n-->51<!--/n--> film styles, each with a short film made entirely in code.**<br>
Pick a style, bring your own story, and let your coding agent direct the film.<br>
<sub><!--n-->51<!--/n--> 种影片风格，每种都配一支完全用代码做出来的短片 · 🇨🇳 中文用户请看 <a href="README.zh-CN.md">简体中文说明</a></sub>

<a href="https://lemomo-ai.github.io/lemo-opuscar/"><img alt="Watch the gallery" src="https://img.shields.io/badge/-%E2%96%B6%20Watch%20the%20gallery-E8553A?style=for-the-badge"></a> <a href="README.zh-CN.md"><img alt="简体中文" src="https://img.shields.io/badge/README-%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-555?style=for-the-badge"></a> <a href="https://github.com/lemomo-ai/lemo-opuscar/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/lemomo-ai/lemo-opuscar?style=for-the-badge&color=F5B700&label=stars"></a> <a href="#licence"><img alt="MIT · CC BY 4.0" src="https://img.shields.io/badge/licence-MIT%20%C2%B7%20CC%20BY%204.0-2EA44F?style=for-the-badge"></a>

⚠️ **Built for Claude.** The styles are tuned for Claude Opus 5.5;<br>
other models may not reproduce them well, so use them with care.

🆕 **2026-10-19 · [Make a style your own](#make-a-style-your-own)**: change a style, give it your own name, get a 15–30 s test film.<br>
🆕 **2026-10-16 · [Evidence Films](https://lemomo-ai.github.io/lemo-opuscar/#evidence-films)**: 8 new styles that film real material, every number measured or sourced. [See them ↓](#evidence-films)

<sub>Official repo: [github.com/lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) · by Lemomo ([@lemomo_ai](https://x.com/lemomo_ai))</sub>

</div>

## 🎬 Feature presentation: OPUSCAR 98

<table><tr>
<td width="50%" valign="top"><a href="https://lemomo-ai.github.io/lemo-opuscar/opuscar98/"><img src="docs/opuscar98.jpg" alt="OPUSCAR 98 — 98 Years of Best Picture"></a><br><b>▶ The film</b> · 1927 – 2025 · 6:31<br><sub>One Clawd walks through all 98 Best Picture winners, each one redrawn in a style that fits the film.</sub></td>
<td width="50%" valign="top"><a href="https://lemomo-ai.github.io/lemo-opuscar/opuscar98/#styles"><img src="docs/opuscar98-styles.jpg" alt="OPUSCAR 98 — all 98 styles open"></a><br><b>All 98 styles, open</b> · 77 in 2D · 4 in 2.5D · 17 in 3D<br><sub>Each film's style tag, a frame, a style prompt to reuse on your own topic, and the shots and direction. Also as <a href="https://lemomo-ai.github.io/lemo-opuscar/opuscar98/styles.json">JSON</a>.</sub></td>
</tr></table>

<div align="center">

Every frame, every note and every cut was written in code by Claude Opus 5.5.<br>
[**▶ Watch**](https://lemomo-ai.github.io/lemo-opuscar/opuscar98/) · [**All 98 styles**](https://lemomo-ai.github.io/lemo-opuscar/opuscar98/#styles) · [**Download 1080p**](https://github.com/lemomo-ai/lemo-opuscar/releases/download/films/opuscar98.mp4)

</div>

## 👋 About me

I'm **Lemomo** ([@lemomo-ai](https://github.com/lemomo-ai)). More about me on my profile.

> **Not an awesome list.** Every film here was made by me, with Claude Opus 5.5.<br>
> The styles are tuned for Opus 5.5; other models may not reproduce them.

![All styles](docs/cover.jpg)

Every film was directed, drawn, scored and mixed by an AI agent writing code:

- 🎨 **Picture**: canvas and WebGL pages, rendered frame by frame
- 🎵 **Music**: original scores from free sample libraries
- 🎙️ **Voice**: text-to-speech narration

No video generation, no stock footage.

## How to use

Two ways in; the skill is the easiest.

### Option 1: install the skill (recommended)

In your terminal:

```sh
claude plugin marketplace add lemomo-ai/lemo-opuscar
claude plugin install lemo-opuscar@lemolab
```

Then use it from any folder.

- On first use it downloads the guides, tools and style prompts to `~/lemo-opuscar`, shared by all your films.
- Each film's project, from source to finished video, goes in the folder you started from.
- For other agents, copy [`plugin/skills/lemo-opuscar/`](plugin/skills/lemo-opuscar/) into their skills folder.

### Option 2: clone the repo

```sh
git clone https://github.com/lemomo-ai/lemo-opuscar.git
cd lemo-opuscar
claude
```

Films go into `films/<name>/` inside the repo.

### Then just say what you want

> Make a 45-second film in the **watercolor** style about the coffee farm my family runs. Warm female narrator.

> Make a 40-second **LiDAR Survey** film about the old quarry in the hills behind our town, from public laser-scan data.

Name the style in English or Chinese; the [style index](styles/README.md) lists them all.

It asks you once, up front:

- anything it can't decide about your topic;
- whether you have your own **voice, music or other material**;
- whether you want to see a **storyboard** first. Say yes and it stops once to show you the key shots in the real style; otherwise it goes straight to the finished film.

The agent reads three guides and works like a small studio:

| File | What it gives the agent |
|---|---|
| [`DIRECTOR.md`](DIRECTOR.md) | how to direct: 