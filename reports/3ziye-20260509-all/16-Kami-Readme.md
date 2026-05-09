<div align="center">
  <img src="https://gw.alipayobjects.com/zos/k/vl/logo.svg" width="120" />
  <h1>Kami</h1>
  <p><b>Good content deserves good paper.</b></p>
  <a href="https://github.com/tw93/kami/stargazers"><img src="https://img.shields.io/github/stars/tw93/kami?style=flat-square" alt="Stars"></a>
  <a href="https://github.com/tw93/kami/releases"><img src="https://img.shields.io/github/v/tag/tw93/kami?label=version&style=flat-square" alt="Version"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License"></a>
  <a href="https://twitter.com/HiTw93"><img src="https://img.shields.io/badge/follow-Tw93-red?style=flat-square&logo=Twitter" alt="Twitter"></a>
</div>

## Why

Kami (紙, かみ) means paper in Japanese: the surface where a finished idea lands. AI can produce documents better than most humans do manually. The missing piece is not capability but constraint: without a design system, every session drifts into generic gray and inconsistent layouts.

Kami fills that gap: one constraint language, eight templates, simple enough for agents to run reliably, strict enough that every output is something you actually want to ship. English and Chinese are first-class; Japanese works via a best-effort CJK path with visual QA before delivery.

Part of a trilogy: [Kaku](https://github.com/tw93/Kaku) (書く) writes code, [Waza](https://github.com/tw93/Waza) (技) drills habits, [Kami](https://github.com/tw93/Kami) (紙) delivers documents.

## See it

<table>
<tr>
  <td align="center" width="25%">
    <a href="assets/demos/demo-tesla.pdf"><img src="assets/demos/demo-tesla.png" alt="Tesla equity report"></a>
    <br><b>Equity Report</b> · 中文
    <br><sub>Tesla Q1 2026 财报点评</sub>
  </td>
  <td align="center" width="25%">
    <a href="assets/demos/demo-agent-slides.pdf"><img src="assets/demos/demo-agent-slides.png" alt="Agent keynote slides" /></a>
    <br><b>Slides</b> · English
    <br><sub>Agent keynote, 6 slides</sub>
  </td>
  <td align="center" width="25%">
    <a href="assets/demos/demo-musk-resume.pdf"><img src="assets/demos/demo-musk-resume.png" alt="Elon Musk resume"></a>
    <br><b>Resume</b> · English
    <br><sub>Founder CV, 2 pages</sub>
  </td>
  <td align="center" width="25%">
    <a href="assets/demos/demo-kaku.pdf"><img src="assets/demos/demo-kaku.png" alt="Kaku portfolio"></a>
    <br><b>Portfolio</b> · 日本語
    <br><sub>Kaku ターミナル作品集 · 7 ページ</sub>
  </td>
</tr>
</table>

## Usage

**Claude Code**

```bash
npx skills add tw93/kami -a claude-code -g -y
```

Or via the Claude Code plugin marketplace:

```bash
/plugin marketplace add tw93/Kami
/plugin install kami@kami
```

**Generic agents** (Codex, OpenCode, Pi, and other tools that read from `~/.agents/`)

```bash
npx skills add tw93/kami -a '*' -g -y
```

**Claude Desktop**

Download [kami.zip](https://github.com/tw93/kami/releases/latest/download/kami.zip), open Customize > Skills > "+" > Create skill, and upload the ZIP directly (no need to unzip).

The ZIP is lightweight: Chinese fonts load from local checkout first, then jsDelivr CDN. If rendering is off, Claude downloads them on the next run. To update: download the same URL, click "..." on the skill card, choose Replace, upload.

The skill auto-triggers from natural requests, no slash command needed. Optimized for English and Chinese; Japanese supported via a best-effort CJK path with visual QA before delivery.

Example prompts by language:

- English: `make a one-pager for my startup` / `turn this research into a long doc` / `write a formal letter` / `make a portfolio of my projects` / `build me a resume` / `design a slide deck for my talk`
- 中文: `帮我做一份一页纸` / `帮我排版一份长文档` / `帮我写一封正式信件` / `帮我做一份作品集` / `帮我做一份简历` / `帮我做一套演讲幻灯片`
- 日本語: `スタートアップ向けの一枚資料を作って` / `この調査を長文レポートに整えて` / `正式な依頼文を作って` / `プロジェクト作品集を作って` / `履歴書を作って` / `登壇用スライドを作って`

**Optional: brand profile**

Create `~/.config/kami/brand.md` to persist identity, brand, defaults, and writing habits. See [brand.example.md](references/brand.example.md) for a full template.

The file has YAML frontmatter (structured fields: name, role, email, website, GitHub, brand color, language, page size, currency locale, tone, and more) plus a Markdown body for freeform notes. Kami treats it as the lowest-resolution context: applied only when the current request is ambiguous, and always overridable by what the specific document needs. The goal is to feel familiar across your work without making every output look the same.

## Design

Warm parchment canvas, ink blue as the sole accent, serif carries hierarchy, no hard shadows or flashy palettes. Not a UI framework; a constraint system for printed matter. Documents should read as composed pages, not dashboards.

Eight document types (One-Pager, Long Doc, Letter, Portfolio, Resume, Slides, Equity Report, Changelog) with dedicated EN/CN templates and a best-effort Japanese path. Fourteen inline SVG diagram types included. Kami picks the right variant based on t