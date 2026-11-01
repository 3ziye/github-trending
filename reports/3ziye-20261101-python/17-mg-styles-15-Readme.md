<div align="center">

# 15 Motion Design Styles

**Fifteen styles, one 10-second film each, all made by Claude Opus 5.5 writing code.**<br>
**15 种 MG 动态设计风格，每种一支 10 秒成片，全部由 Claude Opus 5.5 写代码做出来。**

Every film comes with its style notes, its full prompt and its complete source.<br>
每支片都附风格说明、完整提示词和全部源码。

<a href="https://vincentwei1021.github.io/mg-styles-15/"><img src="docs/readme/cover.webp" width="100%" alt="15 Motion Design Styles: all fifteen films playing side by side"></a>

[**▶ Watch all 15 films with sound · 在线观看**](https://vincentwei1021.github.io/mg-styles-15/)

**English** | [简体中文](README.zh-CN.md)

![films](https://img.shields.io/badge/films-15-ff8a3d) ![length](https://img.shields.io/badge/length-10%20s%20each-555) ![made with](https://img.shields.io/badge/made%20with-Claude%20Opus%205.5-d97757) [![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE) [![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-live-2ea44f)](https://vincentwei1021.github.io/mg-styles-15/)

</div>

> **中文用户请看这里：[完整中文说明 README.zh-CN.md](README.zh-CN.md)**<br>
> English readers: keep reading below.

## What it is

Fifteen 10-second motion-design films, one style each, from frame-by-frame cel animation to a 9:16 variety-show edit. Claude Opus 5.5 made every film by writing code from a prompt: the picture, the animation, the music and the sound effects. This repository publishes all of it, so you can watch a style, read how it was made, copy its prompt and make a film of your own.

- **No image or video generation.** The picture is code: SVG, Canvas, WebGL and Three.js, with Blender for the 3D film. A few films use CC0 or public-domain photos.
- **The sound is code too.** Each film's `audio.py` synthesises its music and sound effects; the 15 soundtracks draw on 103 recorded instrument samples.
- **Everything is published.** The film, the style notes, the full prompt and the complete source, for all 15 styles.

## How a film is made

<p align="center"><img src="docs/readme/flow-en.webp" width="100%" alt="How a film is made: one prompt per style, then Claude writes the film as a web page that can draw any moment, headless Chrome renders every frame, audio.py synthesises the music and effects on the same cues, ffmpeg muxes an exact 10-second MP4, and a second AI reviews it with rubric.md for two rounds of revision"></p>

Every film is a web page that draws the frame for any time you give it (`window.renderAt(t)`). The renderer captures each frame in headless Chrome, then ffmpeg joins the frames and the soundtrack. The 3D film is the one exception: Blender renders its picture, and a web page adds the type and grain. Each film went through two rounds of review and revision. Final scores from the AI jury run from 7.57 to 8.21 out of 10.

## The 15 styles

Click a film to watch it with sound on the page.

<table>
<tr>
<td align="center" valign="top" width="33%"><a href="https://vincentwei1021.github.io/mg-styles-15/#05-cel-boil"><img src="docs/readme/films/05-cel-boil.webp" width="100%" alt="Frame-by-Frame / Line Boil: HAND MADE"></a><br><b>01 · Frame-by-Frame / Line Boil</b><br><sub>HAND MADE</sub><br><sub><a href="prompts/05-cel-boil.md">Prompt</a> · <a href="demos/05-cel-boil">Source</a></sub></td>
<td align="center" valign="top" width="33%"><a href="https://vincentwei1021.github.io/mg-styles-15/#03-isometric"><img src="docs/readme/films/03-isometric.webp" width="100%" alt="Isometric 2.5D: ISOPOLIS — Let the City Grow"></a><br><b>02 · Isometric 2.5D</b><br><sub>ISOPOLIS — Let the City Grow</sub><br><sub><a href="prompts/03-isometric.md">Prompt</a> · <a href="demos/03-isometric">Source</a></sub></td>
<td align="center" valign="top" width="33%"><a href="https://vincentwei1021.github.io/mg-styles-15/#01-flat-vector"><img src="docs/readme/films/01-flat-vector.webp" width="100%" alt="Flat Vector: popwise — One Dot"></a><br><b>03 · Flat Vector</b><br><sub>popwise — One Dot</sub><br><sub><a href="prompts/01-flat-vector.md">Prompt</a> · <a href="demos/01-flat-vector">Source</a></sub></td>
</tr>
<tr>
<td align="center" valign="top" width="33%"><a href="https://vincentwei1021.github.io/mg-styles-15/#02-line-art"><img src="docs/readme/films/02-line-art.webp" width="100%" alt="Line Art: ATELIER LINEA — One Line"></a><br><b>04 · Line Art</b><br><sub>ATELIER LINEA — One Line</sub><br><sub><a href="prompts/02-line-art.md">Prompt</a> · <a href="demos/02-line-art">Source</a></sub></td>
<td align="center" valign="top" width="33%"><a href="https://vincentwei1021.github.io/mg-styles-15/#04-3d-render"><img src="docs/readme/films/04-3d-render.webp" width="100%" alt="3D Render: soft. — Soft Landing · C4D / Blender look"></a><br><b>05 · 3D Render</b><br><sub>soft. — Soft Landing · C4D / Blender look</sub><br><sub><a href="prompts/04-3d-render.md">Prompt</a> · <a href="demos/04-3d-render">Source</a></sub></td>
<td align="center" valign="top" width="33%"><a href="https://vincentwei1021.github.io/mg-styles-15/#08-morph"><img src="do