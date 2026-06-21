# Pixel2Motion - AI Logo Animation Skill

**Raster logo → smooth minimal SVG → SVG logo animation → interactive HTML motion demo.**

[Live interactive demo](https://nolangz.github.io/pixel2motion/) · [Skill instructions](https://github.com/nolangz/pixel2motion/blob/main/SKILL.md) · [Companion skill: Pixel2SVG-HTML](https://github.com/nolangz/pixel2svg-html)

Pixel2Motion is an open-source Codex and Claude skill for **logo animation**, **SVG animation**, and AI-assisted brand motion. It turns PNG, JPG, WebP, or screenshot logos into clean motion-ready SVG, then exports animated logo HTML, GIF/video previews, and motion QA evidence. Use it for animated logos, SVG logo reveals, logo motion design, pixel-to-vector reconstruction, and developer-friendly HTML animation workflows.

中文：Pixel2Motion 是一个把像素 logo 转成平滑 SVG，再生成品牌 motion、logo reveal、HTML 动效展示和视频预览的 Codex skill。它适合需要可审查矢量拟合、可复用 SVG 结构和可导出动图/透明视频的设计与开发场景。

Recommended review order: the motion gallery below, the interactive demo, the fitting evidence, and then the implementation workflow.

## Pixel-to-Motion Gallery

Each pairing shows the raster source next to the motion output, rendered from `docs/index.html` at the animation's default speed: Horizon 1900 ms, Continuum 2000 ms, Focus 1700 ms, N 2400 ms, and CueRecord at the page-default 0.65× custom timeline.

<table>
  <tr>
    <td align="center" width="50%">
      <strong>Horizon</strong><br>
      <sub>Pixel source</sub><br>
      <img src="docs/pixels/horizon-pixel.png" width="260" alt="Horizon pixel source logo"><br>
      <sub>Motion output</sub><br>
      <img src="docs/gifs/claude-horizon.gif" width="320" alt="Claude Horizon logo motion preview">
    </td>
    <td align="center" width="50%">
      <strong>Continuum</strong><br>
      <sub>Pixel source</sub><br>
      <img src="docs/pixels/continuum-pixel.png" width="260" alt="Continuum pixel source logo"><br>
      <sub>Motion output</sub><br>
      <img src="docs/gifs/claude-continuum.gif" width="320" alt="Claude Continuum logo motion preview">
    </td>
  </tr>
  <tr>
    <td align="center" width="50%">
      <strong>CueRecord</strong><br>
      <sub>Pixel source</sub><br>
      <img src="docs/pixels/cuerecord-pixel.jpg" width="300" alt="CueRecord pixel source logo"><br>
      <sub>Motion output</sub><br>
      <img src="docs/gifs/claude-cuerecord.gif" width="320" alt="Claude CueRecord logo motion preview">
    </td>
    <td align="center" width="50%">
      <strong>N</strong><br>
      <sub>Pixel source</sub><br>
      <img src="docs/pixels/n-pixel.png" width="320" alt="N pixel source logo"><br>
      <sub>Motion output</sub><br>
      <img src="docs/gifs/claude-n.gif" width="320" alt="Claude N logo motion preview">
    </td>
  </tr>
  <tr>
    <td align="center" width="50%">
      <strong>Focus</strong><br>
      <sub>Pixel source</sub><br>
      <img src="docs/pixels/focus-pixel.png" width="260" alt="Focus pixel source logo"><br>
      <sub>Motion output</sub><br>
      <img src="docs/gifs/claude-focus.gif" width="320" alt="Claude Focus logo motion preview">
    </td>
    <td align="center" width="50%"></td>
  </tr>
</table>

## Interactive Demo

[![Pixel2Motion project preview](docs/preview.png)](https://nolangz.github.io/pixel2motion/)

The full interactive showcase lives in `docs/index.html` and is published through GitHub Pages at `https://nolangz.github.io/pixel2motion/`.

## Fitting Evidence

Every animation is authored against a QA-verified static vector. The CueRecord fitting sequence, read left to right:

![CueRecord overlay progress strip](docs/process/cuerecord-overlay-progress-strip.png)

The teal overlays are QA checkpoints, not the deliverable: the vector candidate is repeatedly compared against the raster source until mark scale, dot placement, wordmark baseline, and ink weight hold up — and only then is motion authored on top. The resulting clean semantic SVG, with mark, dot, and wordmark as separate addressable parts, becomes the final-frame contract for the animation.

Pixel2Motion optimizes IoU as a diagnostic, but smoothness and structure are the hard gates. A high-IoU jagged trace is rejected when a lower-complexity smooth vector explains the logo better. The static fitting methodology is documented in full in the companion [Pixel2SVG-HTML](https://github.com/nolangz/pixel2svg-html) project.

## Deliverables

- `logo.svg`: final static vector, structured for motion
- `motion.css`: authored choreography targeting semantic SVG ids
- `logo_motion.html`: dependency-free showcase HTML with replay, slow motion, speed control, QA hooks, and atomic motion studies
- `motion_spec.md`: motion brief, principles applied, timeline, easing tokens, and QA notes
- `outputs/fit_iterations/*.png`: geometry overlay evidence
- `outputs/motion_frames/*.png` and `outputs/motion_strip.png`: deterministic motion QA evidence
- `outputs/final_render.png` and `outputs/html_render.png`: static render checks

## Workflow

1. Read `SKILL.md` and the re