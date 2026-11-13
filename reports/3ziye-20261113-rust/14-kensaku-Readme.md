<p align="center">
  <img src="assets/icon.png" width="112" height="112" alt="Kensaku" />
</p>

<h1 align="center">Kensaku <span title="kensaku = search, in Japanese">検索</span></h1>

<p align="center">
  <b>Fast, light, and efficient. Find anything on your computer.</b>
</p>

<p align="center">
  Search 100,000 file names in milliseconds, with about 12 MB of metadata.<br/>
  Search inside documents, images, and code too. Nothing leaves your machine.
</p>

<p align="center">
  <a href="https://upstar.dev/r/yjid/kensaku"><img alt="Upstar trending" src="https://upstar.dev/badge/yjid/kensaku.svg" /></a>
</p>

<p align="center">
  <a href="https://github.com/yjid/kensaku/releases/latest"><img alt="Latest release" src="https://img.shields.io/github/v/release/yjid/kensaku?style=for-the-badge" /></a>
  <a href="https://github.com/yjid/kensaku/releases/latest"><img alt="Downloads" src="https://img.shields.io/github/downloads/yjid/kensaku/total?style=for-the-badge" /></a>
  <a href="LICENSE"><img alt="MIT license" src="https://img.shields.io/badge/license-MIT-111111?style=for-the-badge" /></a>
  <a href="https://github.com/yjid/kensaku/actions/workflows/ci.yml"><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/yjid/kensaku/ci.yml?branch=master&style=for-the-badge" /></a>
</p>

<p align="center">
  <a href="#install">Install</a> ·
  <a href="#what-kensaku-does-that-the-others-dont">Why Kensaku</a> ·
  <a href="#features">Features</a> ·
  <a href="#performance">Performance</a> ·
  <a href="#connect-ai-agents-mcp">MCP</a> ·
  <a href="docs/README.md">Docs</a> ·
  <a href="docs/LANGUAGES.md">Languages</a> ·
  <a href="#contributing">Contribute</a>
</p>

<p align="center">
  <img src="assets/hero.png" width="100%" alt="Kensaku — find anything on your computer" />
</p>

---

## Find it the way you remember it

You don't remember the filename. You remember what was in it.

- The PDF about database indexing, saved as `notes-final-2.pdf`.
- The log line from the failed deploy, somewhere in a folder of logs.
- The screenshot with a CUDA error, which has no useful name at all.

Type what you remember. Kensaku searches names, text inside files, and meaning, and shows the match with the words highlighted. Open it with Enter.

## What Kensaku does that the others don't

Filename tools are everywhere. Reading *inside* your files — locally, instantly, and for free — is not.

| | Kensaku | Everything | Listary | PowerToys Run |
|---|---|---|---|---|
| Filename search, milliseconds | ✅ | ✅ | ✅ | ✅ |
| Full text inside PDF/DOCX/EPUB… | ✅ | ❌ | ❌ | ❌ |
| Text inside screenshots & images (OCR) | ✅ | ❌ | ❌ | ❌ |
| Multilingual & CJK text (auto-tokenized) | ✅ | ❌ | ❌ | ❌ |
| Find by meaning ("the PDF about indexing") | ✅ | ❌ | ❌ | ❌ |
| Natural-language time ("screenshots from last week") | ✅ | ❌ | partial | ❌ |
| Your AI agents can search it (MCP) | ✅ | ❌ | ❌ | ❌ |
| Launcher behavior (summon, type, Enter) | ✅ | ❌ | ✅ | ✅ |
| Open source (MIT) | ✅ | ❌ | ❌ | ✅ |

*Spotlight and Raycast are excellent but macOS-only; Alfred's content search and AI are paid tiers. Kensaku is one app, three platforms, free and MIT-licensed.*

**Three things worth trying on day one:**

1. **Screenshot archaeology.** You know you saw that error in a screenshot. Kensaku read the pixels — search the error text.
2. **Describe, don't recall.** "big videos from last month" is a valid query. No filters to click.
3. **Give your AI agent eyes.** Claude or Cursor can search this same index over MCP — read-only, local, no cloud.

## Features

**Fast**
- Filename search across ~100,000 files in milliseconds on a warm cache. Method, hardware, and per-platform numbers are in [Performance](#performance).
- Results update as you type. There is no separate search page.
- Incremental indexing: changed files are picked up without rescanning the whole disk.
- Closing the window keeps the index warm; reopening is instant.

**Finds more**
- Names, full text, fuzzy matches that tolerate typos, and meaning, in one search.
- **Documents & Office**: PDF, DOCX, PPTX, XLSX, EPUB, ODT/ODS/ODP, RTF, CSV/TSV, email (`.eml`, `.msg`), and plain text.
- **Multilingual & CJK by default**: Custom unigram + bigram tokenizer for Chinese (Hanzi/Bopomofo), Japanese (Kanji/Kana), and Korean (Hangul), plus mixed-script boundary handling. Detailed breakdown in [docs/LANGUAGES.md](docs/LANGUAGES.md).
- **50+ Code & Data Formats**: Rust, Python, TypeScript, Go, C/C++, Java, Shell, SQL, JSON, YAML, TOML, Dockerfile, and more.
- **Images & OCR**: Text is read with PP-OCRv6 by default (bundled runtime; the ~6.1 MB model pack downloads once). Higher-quality Indra engine (deskew, multi-script Latin/CJK/RTL/World recognition, ~27 MB pack) and classic Tesseract are selectable in Setup/Settings.
- **Content depth you can tune**: up to 100 MB per file, 4 MB of text, and 48 semantic chunks by default; `quick` / `balanced` / `deep` presets.

**Precise**
- Filters and sort: Best match, Newest, 