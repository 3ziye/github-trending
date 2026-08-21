<p align="center">
  <picture>
    <source
      media="(prefers-color-scheme: dark)"
      srcset="assets/moli-browser-banner-dark.jpg"
    />
    <source
      media="(prefers-color-scheme: light)"
      srcset="assets/moli-browser-banner.jpg"
    />
    <img
      src="assets/moli-browser-banner.jpg"
      alt="Moli Browser — Structure first. Pixels on demand. Open source browser for AI agents."
      width="1086"
    />
  </picture>
</p>

<h1 align="center">Moli</h1>

<p align="center">
  <strong>English</strong> |
  <a href="docs/README.zh-CN.md">简体中文</a> |
  <a href="docs/README.ja.md">日本語</a> |
  <a href="docs/README.de.md">Deutsch</a> |
  <a href="docs/README.fr.md">Français</a> |
  <a href="docs/README.es.md">Español</a>
</p>

Moli is a production-ready headless browser for AI agents. Its on-demand layout
and rendering design combines a complete browser runtime with a lightweight
resource footprint.

Moli helps your AI agent fetch and extract web pages, search the web, and
automate browser tasks.

Use it through the CLI, CDP, WebDriver Classic, or WebDriver BiDi.

Moli supports Linux, macOS, and Windows.

## Quick start

Give this prompt to your AI agent:

```text
Install the skills under https://github.com/lexmount/moli/tree/main/skills,
follow their instructions to download and install the latest prebuilt Moli
binary, then use moli-webfetch to fetch https://example.com and show me the
result.
```

### Direct installation

On Linux or macOS:

```sh
curl --proto '=https' --tlsv1.2 -fsSL \
  https://github.com/lexmount/moli/releases/latest/download/moli-installer.sh | sh
```

On Windows, run in PowerShell:

```powershell
irm https://github.com/lexmount/moli/releases/latest/download/moli-installer.ps1 | iex
```

## Showcase

<p align="center">
  <a href="assets/moli-game.jpg">
    <img
      src="assets/moli-game.jpg"
      alt="An HTML5 game rendered by Moli and inspected through Chrome DevTools"
      width="1200"
    />
  </a>
</p>

<p align="center">
  <sub>An HTML5 game rendered by Moli and inspected live through Chrome DevTools.</sub>
</p>

<p align="center">
  <a href="assets/moli-devtools-rust-lang.jpg">
    <img
      src="assets/moli-devtools-rust-lang.jpg"
      alt="rust-lang.org rendered by Moli and inspected through Chrome DevTools"
      width="1200"
    />
  </a>
</p>

<p align="center">
  <sub>rust-lang.org rendered by Moli, with its live DOM, CSS, and geometry available in Chrome DevTools.</sub>
</p>

## CLI usage

### Extract a page

Render the page as Markdown with Moli's default completion strategy:

```bash
moli fetch \
  --dump markdown \
  --wait-until done \
  https://example.com
```

Or directly return a compact, model-friendly semantic tree:

```bash
moli fetch \
  --dump semantic_tree_text \
  --wait-selector body \
  https://example.com
```

For visual output, enable on-demand layout and write a viewport PNG, a full-document PNG, or a paginated PDF:

```bash
moli fetch --layout --dump screenshot https://example.com > page.png
moli fetch --layout --dump screenshot_full https://example.com > full-page.png
moli fetch --layout --dump pdf https://example.com > page.pdf
```

Run `fetch --help` for the complete option list, including output formats,
page-load/response waits, profiles, proxy settings, resource policies, and
tracing options.

### Start the automation server

```bash
# Basic automation server for DOM-first workloads
moli serve

# Enable real geometry, coordinate input, and screenshot/screencast surfaces
moli serve --layout

# Also fetch optional image, font, audio, video, media, and text-track resources
moli serve --layout --resource
```

The same endpoint serves all three protocols: CDP, WebDriver Classic, and
WebDriver BiDi. Playwright can connect directly over CDP:

```js
import { chromium } from "playwright";

const browser = await chromium.connectOverCDP("http://127.0.0.1:9222");
const context = browser.contexts()[0];
const page = context.pages()[0] ?? await context.newPage();

await page.goto("https://example.com");
console.log(await page.locator("body").innerText());

await browser.close();
```

## Why Moli

Three qualities matter most for agent workloads, and Moli brings them together:

- **Full-featured** — real JavaScript, DOM, CSS, networking, storage, layout,
  screenshots, and standard automation protocols, all integrated into one
  headless browser.
- **Fast** — most automation requests never need visual rendering, so
  structure-first operations skip layout and paint entirely.
- **Resource-efficient** — layout and pixels are generated only when needed,
  so Moli does not have to continuously maintain and update a fully rendered
  visual state.

What most browser automation tasks actually need is page structure, not a
continuously rendered visual world. Moli treats the native DOM and style state
as the single source of truth, triggering layout or software paint only for
operations that genuinely require them.

| Agent request | What Moli does |
| --- 