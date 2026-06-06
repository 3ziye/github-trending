# HTML Anything

<p align="center"><sub>From the team behind <a href="https://github.com/nexu-io/open-design"><b>Open Design</b></a> — <b>40k★ · 200+ contributors</b>, production-grade and iterating faster. html-anything is the focused agent-era HTML editor; if it clicks for you, <a href="https://github.com/nexu-io/open-design">Open Design</a> is where the same team ships at scale.</sub></p>

<p align="center"><b>Live page:</b> <a href="https://open-design.ai/html-anything/"><b>open-design.ai/html-anything/</b></a> — overview, surface modes, and showcase before you clone.</p>

> **Markdown is the draft. HTML is what humans read. Your local agent writes it.** The agentic HTML editor — in the agentic era, you don't hand-edit docs anymore, so the output format should be what the reader actually wants: HTML. Local-first, zero API key, reuses the CLI session you already have logged in — **8 coding-agent CLIs** auto-detected on your `PATH` (Claude Code · Cursor Agent · Codex · Gemini CLI · GitHub Copilot CLI · OpenCode · Qwen Coder · Aider), driven by **75 composable skill templates** across **9 deliverable surfaces** (magazine articles · keynote decks · résumés · posters · Xiaohongshu cards · tweet cards · web prototypes · data reports · Hyperframes videos). One-click export to WeChat / X / Zhihu, or download `.html` / `.png`.

<p align="center">
  <img src="docs/assets/banner.png" alt="HTML Anything — the agentic HTML editor, on your laptop" width="100%" />
</p>

<p align="center">
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-Apache%202.0-blue.svg?style=flat-square" /></a>
  <a href="#supported-coding-agents"><img alt="Agents" src="https://img.shields.io/badge/agents-8%20CLIs-black?style=flat-square" /></a>
  <a href="#skills"><img alt="Skills" src="https://img.shields.io/badge/skills-75-orange?style=flat-square" /></a>
  <a href="#export-targets"><img alt="Export" src="https://img.shields.io/badge/export-WeChat%20%C2%B7%20X%20%C2%B7%20Zhihu%20%C2%B7%20PNG-9b59b6?style=flat-square" /></a>
  <a href="#quickstart"><img alt="Quickstart" src="https://img.shields.io/badge/quickstart-30%20seconds-green?style=flat-square" /></a>
  <a href="#architecture"><img alt="No API key" src="https://img.shields.io/badge/no-API%20key%20required-ff6b35?style=flat-square" /></a>
</p>

<!-- This project is built on top of nexu-io/open-design — the badges below link to its community channels on purpose. -->
<p align="center">
  <a href="https://discord.gg/keeVPMrueT"><img alt="Discord (html-anything)" src="https://img.shields.io/badge/discord-html--anything-5865f2?style=flat-square&logo=discord&logoColor=white" /></a>
  <a href="https://x.com/nexudotio"><img alt="Follow @nexudotio on X" src="https://img.shields.io/badge/follow-%40nexudotio-000000?style=flat-square&logo=x&logoColor=white" /></a>
  <a href="https://github.com/nexu-io/open-design/releases/latest"><img alt="open-design release" src="https://img.shields.io/github/v/release/nexu-io/open-design?style=flat-square&label=release&color=8e44ad" /></a>
  <a href="https://github.com/nexu-io/open-design/graphs/commit-activity"><img alt="open-design commits / month" src="https://img.shields.io/github/commit-activity/m/nexu-io/open-design?style=flat-square&label=commits%2Fmonth&color=f39c12" /></a>
  <a href="#showcase"><img alt="Design systems" src="https://img.shields.io/badge/design%20systems-9-1abc9c?style=flat-square" /></a>
  <a href="https://github.com/nexu-io/open-design"><img alt="Built on open-design" src="https://img.shields.io/badge/built%20on-nexu--io%2Fopen--design-ff7043?style=flat-square&logo=github&logoColor=white" /></a>
</p>

<p align="center"><b>English</b> · <a href="README.zh-CN.md">简体中文</a></p>

---

## Showcase

The eight skills that surface at the top of the picker's **Featured / 推荐** group — sorted by their `recommended:` rank in `SKILL.md` frontmatter (lower = higher). Each ships a real `example.html` you can open straight from the repo, no auth, no setup.

<table>
<tr>
<td width="50%" valign="top">
<a href="next/src/lib/templates/skills/deck-guizang-editorial/"><img src="docs/screenshots/skills/deck-guizang-editorial.png" alt="deck-guizang-editorial" /></a><br/>
<sub><b><a href="next/src/lib/templates/skills/deck-guizang-editorial/"><code>deck-guizang-editorial</code></a></b> · <i>deck</i> · <code>recommended: 1</code><br/>Magazine × e-ink editorial deck, inspired by <a href="https://github.com/op7418/guizang-ppt-skill"><code>op7418/guizang-ppt-skill</code></a> — 10 locked layouts × 5 palettes (Ink / Indigo Porcelain / Forest Ink / Kraft / Dune). Reads like a printed art-zine, not a slide deck.</sub>
</td>
<td width="50%" valign="top">
<a href="next/src/lib/templates/skills/deck-swiss-international/"><img src="docs/screenshots/skills/deck-swiss-international.png" alt="deck-swiss-international" /></a><br/>
<sub><b><a href="next/src/lib/templates/skills/deck-swiss-international/"><code>deck-swiss-international</code></a></