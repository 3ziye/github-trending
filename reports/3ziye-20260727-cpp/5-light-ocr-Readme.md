# light-ocr

[![Core CI](https://github.com/arcships/light-ocr/actions/workflows/core.yml/badge.svg?branch=main)](https://github.com/arcships/light-ocr/actions/workflows/core.yml)
[![License](https://img.shields.io/github/license/arcships/light-ocr)](LICENSE)
[![C++17](https://img.shields.io/badge/C%2B%2B-17-00599C.svg)](https://isocpp.org/)
[![Node--API v8](https://img.shields.io/badge/Node--API-v8-339933.svg)](bindings/node/README.md)
[![npm](https://img.shields.io/npm/v/%40arcships%2Flight-ocr?color=CB3837)](https://www.npmjs.com/package/@arcships/light-ocr)

<a href="https://trendshift.io/repositories/82168?utm_source=trendshift-badge&amp;utm_medium=badge&amp;utm_campaign=badge-trendshift-82168" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/trendshift/repositories/82168/daily?language=C%2B%2B" alt="arcships%2Flight-ocr | Trendshift" width="250" height="55"/></a>

English | [简体中文](README.zh-CN.md)

![light-ocr pixel-art banner](docs/assets/light-ocr-banner.png)

**Fast, offline OCR for Node.js and C++.**

Recognize text in JPEG, PNG, or raw image data directly on your machine. `light-ocr` returns lines in reading order with confidence scores and quadrilateral coordinates. For Node.js, the npm package includes PP-OCRv6 Small and prebuilt components for macOS, Linux, and Windows.

## Quick start

Node.js 22 and 24 are supported.

```bash
npm install @arcships/light-ocr
```

```ts
import { createEngine } from "@arcships/light-ocr";
import { readFile } from "node:fs/promises";

const engine = await createEngine();
const result = await engine.recognizeEncoded(
  await readFile("image.jpg"),
);

for (const line of result.lines) {
  console.log(line.text, line.confidence, line.box);
}

await engine.close();
```

`createEngine()` automatically chooses the right execution mode for the current platform. If your application already decodes images, [`recognize()`](bindings/node/README.md#usage) also accepts `GRAY8`, `RGB8`, `BGR8`, and `RGBA8` pixel data.

### Model tiers

Small remains the stable default. N2 also provides two opt-in preview packages under the `next` tag; all three expose the same API, types, result schema, and error model, while each install contains only its selected model.

| Tier | Package / command | Model payload | Status |
| --- | --- | ---: | --- |
| Small | `@arcships/light-ocr` / `light-ocr` | ~30 MB | stable default |
| Tiny | `@arcships/light-ocr-tiny@next` / `light-ocr-tiny` | ~6.3 MB | preview; 49 languages, no Japanese |
| Medium | `@arcships/light-ocr-medium@next` / `light-ocr-medium` | ~139 MB | preview; quality-first |

Tiny and Medium stay on `next` until real use shows a clear reason to promote them; they do not change what `npm install @arcships/light-ocr` installs.

## CLI

The `light-ocr` command is available after install — no extra setup:

```bash
# Recognize text + coordinates
light-ocr image.png --format json

# Just text
light-ocr image.png --format text

# Detect text regions only (no recognition)
light-ocr detect image.png

# Region of interest
light-ocr recognize image.png --region 100,80,640,320 --format json

# Engine info
light-ocr info --version

# System diagnostics (hardware and providers)
light-ocr doctor --json
```

Four subcommands: `recognize` (default), `detect` (boxes only), `info` (version diagnostics), and `doctor` (system diagnostics). Output wraps in a versioned `schemaVersion: 1` envelope with stable line/detection IDs. EXIF orientation is corrected automatically. See the [CLI design](docs/cli-design.md) and [npm README](bindings/node/README.md#cli) for full reference.

### PDF and multi-page documents

PDF and multi-page OCR live in an explicit preview package so the stable default keeps its script-free, offline-installable dependency closure. Installing the preview runs `pdfium-native`'s verified prebuild installer; PDF processing itself stays local.

```bash
npm install @arcships/light-ocr-document@next

# Single PDF with default 150 DPI
light-ocr-document report.pdf

# Page range with streaming JSONL output
light-ocr-document report.pdf --pages 1-10 --format jsonl

# Multiple images as one document
light-ocr-document scan1.png scan2.png scan3.png --format text
```

Programmatic API:

```ts
import { recognizeDocument } from "@arcships/light-ocr-document";

// Stream pages from a PDF
for await (const page of recognizeDocument("report.pdf", { dpi: 200 })) {
  console.log(page.index, page.lines.length, page.source.kind);
}

// Multiple images
for await (const page of recognizeDocument([buf1, buf2, buf3])) {
  console.log(page.index, page.lines);
}
```

## Agent Skill

An [Agent Skill](.agents/skills/local-ocr/SKILL.md) is included for AI agents that can call local commands. It provides scenario-driven workflows, a decision flow for command selection, and exit code reference:

- When to use OCR vs. a multimodal model
- Detect-then-recognize two-step pattern for large images
- ROI field extraction for receipts and fo