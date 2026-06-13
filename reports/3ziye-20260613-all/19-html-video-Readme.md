# html-video

<p align="center">
  <img src="docs/assets/hero.png" alt="html-video — HTML becomes video, on your laptop" width="100%" />
</p>

> **HTML becomes video — on your laptop.** Bring your local coding agent (Open Design · Windsurf CLI · Trae CLI · Claude Code · Cursor · Codex · Gemini · Grok · Qwen · OpenCode · Copilot · Aider · Hermes · or the Anthropic API). Describe a video, or **paste an article link / GitHub repo**, and the agent turns it into a multi-frame, fully animated video — then renders it to a real MP4 right on your machine. One agent loop, pluggable rendering engines, a curated template gallery, optional AI soundtrack. Apache-2.0, no per-render fees, no vendor lock-in.

<p align="center">
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-Apache%202.0-blue.svg?style=flat-square" /></a>
  <a href="#supported-agents"><img alt="Agents" src="https://img.shields.io/badge/agents-14%20backends-111?style=flat-square" /></a>
  <a href="#showcase"><img alt="Templates" src="https://img.shields.io/badge/templates-21-3ce6ac?style=flat-square" /></a>
  <a href="#turn-a-link-into-a-video"><img alt="Sources" src="https://img.shields.io/badge/from-article%20%C2%B7%20repo%20%C2%B7%20prompt-9b59b6?style=flat-square" /></a>
  <a href="#soundtrack"><img alt="Soundtrack" src="https://img.shields.io/badge/soundtrack-AI%20music%20%2B%20narration-e67e22?style=flat-square" /></a>
  <a href="#quick-start"><img alt="Quickstart" src="https://img.shields.io/badge/quickstart-3%20commands-22a34a?style=flat-square" /></a>
</p>

<!-- Built by the team behind Open Design — these link to its community on purpose. -->
<p align="center">
  <a href="https://github.com/nexu-io/open-design#community"><img alt="Discord" src="https://img.shields.io/badge/discord-join-5865f2?style=flat-square&logo=discord&logoColor=white" /></a>
  <a href="https://x.com/nexudotio"><img alt="Follow @nexudotio on X" src="https://img.shields.io/badge/follow-%40nexudotio-000000?style=flat-square&logo=x&logoColor=white" /></a>
  <a href="https://github.com/nexu-io/open-design"><img alt="By the Open Design team" src="https://img.shields.io/badge/by-nexu--io%2Fopen--design-ff7043?style=flat-square&logo=github&logoColor=white" /></a>
</p>

<p align="center">
  <b>An official project by the <a href="https://open-design.ai">Open Design</a> team</b> · <a href="https://open-design.ai">open-design.ai</a>
</p>

<p align="center"><b>English</b> · <a href="README.zh-CN.md">简体中文</a></p>

---

## Showcase

Every template below is a real, animated single-file HTML video — these are live renders, not mockups. Drop one in, let the agent fill it with your content, export to MP4.

<table>
<tr>
<td width="50%"><img src="docs/assets/templates/frame-data-chart-nyt.png" alt="NYT-style data chart" /></td>
<td width="50%"><img src="docs/assets/templates/frame-glitch-title.png" alt="Glitch title" /></td>
</tr>
<tr>
<td><b>frame-data-chart-nyt</b> · data-viz<br/>Editorial NYT-style animated line chart — headline, annotated data points, source line. For "the number went up" stories.</td>
<td><b>frame-glitch-title</b> · title card<br/>Chromatic-aberration glitch title with scanlines. For openers, drops, and "system online" energy.</td>
</tr>
<tr>
<td><img src="docs/assets/templates/frame-liquid-bg-hero.png" alt="Liquid background hero" /></td>
<td><img src="docs/assets/templates/frame-light-leak-cinema.png" alt="Light leak cinema" /></td>
</tr>
<tr>
<td><b>frame-liquid-bg-hero</b> · hero<br/>Aurora liquid-gradient hero with a centered headline. For product reveals and bold statements.</td>
<td><b>frame-light-leak-cinema</b> · cinematic<br/>Warm film-grain + light-leak cinematic frame. For mood, brand films, "a quiet year" storytelling.</td>
</tr>
<tr>
<td><img src="docs/assets/templates/vfx-text-cursor.png" alt="Typewriter cursor VFX" /></td>
<td><img src="docs/assets/templates/frame-logo-outro.png" alt="Logo outro" /></td>
</tr>
<tr>
<td><b>vfx-text-cursor</b> · VFX<br/>Typewriter text with a blinking terminal cursor. For code-style reveals and CLI demos.</td>
<td><b>frame-logo-outro</b> · outro<br/>Clean animated logo end card. For sign-offs and brand stamps at the end of any video.</td>
</tr>
</table>

…and 15 more, including multi-scene product promos, kinetic type, Swiss-grid and Vignelli data cards, decision-tree explainers, Takram-organic motion, and warm-grain editorial. Browse all 21 live in the studio gallery.

---

## Why this exists

HTML→Video is a real category — but every engine is opinionated, and each wants you to learn *its* authoring model:

| Engine | Paradigm | Tradeoff | In html-video |
|---|---|---|---|
| [Hyperframes](https://github.com/heygen-com/hyperframes) | HTML + CSS + GSAP, agent-skill driven | Single rendering paradigm | ✅ **Shipped** — the default engine; renders real MP4 via headless Chromium + ffmpeg |
| [Remotion](https://www.remotion.dev/) | React components | Source-available, paid above 4 devs | 🗺️ Planned |
