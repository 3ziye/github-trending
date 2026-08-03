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

Recognize text in PDF, JPEG, PNG, or raw image data directly on your machine.
`light-ocr` returns lines in reading order with confidence scores and
quadrilateral coordinates. The Node.js package includes PP-OCRv6 Small,
PDFium, a Chinese fallback font, and prebuilt components for macOS, Linux, and
Windows—without postinstall or first-run downloads.

| | |
| --- | --- |
| **Best for** | local OCR in Node.js apps, CLIs, desktop software, and native C++ integrations |
| **Inputs** | JPEG, PNG, PDF, encoded bytes, or decoded pixel buffers |
| **Outputs** | text, confidence, quadrilateral boxes, page metadata, and timing |
| **Distribution** | one npm install; CommonJS, ESM, TypeScript, and six prebuilt platforms |

## Quick start

Node.js 22 and 24 are supported.

```bash
npm install @arcships/light-ocr
```

```ts
import { createEngine } from "@arcships/light-ocr";
import { readFile } from "node:fs/promises";

const engine = await createEngine();

try {
  const result = await engine.recognizeEncoded(
    await readFile("image.jpg"),
  );

  for (const line of result.lines) {
    console.log(line.text, line.confidence, line.box);
  }
} finally {
  await engine.close();
}
```

`createEngine()` automatically chooses the right execution mode for the
current platform. If your application already decodes images,
[`recognize()`](packages/light-ocr/README.md#recognize-decoded-pixels) also
accepts `GRAY8`, `RGB8`, `BGR8`, and `RGBA8` pixel data.

PDF pages use the same package:

```ts
import { recognizeDocument } from "@arcships/light-ocr";

for await (const page of recognizeDocument("report.pdf", { dpi: 200 })) {
  console.log(page.index, page.lines.map((line) => line.text));
}
```

CommonJS uses the same exports through `require("@arcships/light-ocr")`.

## CLI

The `light-ocr` command is available after install — no extra setup:

```bash
# Recognize text + coordinates
light-ocr image.png --format json

# Just text
light-ocr image.png --format text

# PDF pages, using the renderer already included by npm
light-ocr report.pdf --pages 1-10 --format text

# Detect text regions only (no recognition)
light-ocr detect image.png

# Region of interest
light-ocr recognize image.png --region 100,80,640,320 --format json

# Engine info
light-ocr info --version

# System diagnostics (hardware and providers)
light-ocr doctor --json
```

Image commands are `recognize` (default), `detect` (boxes only), `info`
(version diagnostics), and `doctor` (system diagnostics). A `.pdf` path routes
directly to document OCR; `document` handles explicit multi-source jobs. Output
uses a versioned `schemaVersion: 1` contract. EXIF orientation is corrected
automatically. See the [CLI design](docs/cli-design.md) and
[npm package README](packages/light-ocr/README.md) for the complete
install-and-use reference.

## PDF and multi-page documents

PDF and multi-page OCR are built into `@arcships/light-ocr`. The matching
PDFium binary and checksum-pinned Noto Sans SC fallback font are carried by
the same platform npm package as the OCR runtime. This keeps PDFs that reference
common non-embedded Chinese fonts renderable before OCR, with no postinstall
script, runtime download, compiler, system-font requirement, or separate
package to install.

```bash
# Single PDF with default 150 DPI
light-ocr report.pdf

# Page range with streaming JSONL output
light-ocr report.pdf --pages 1-10 --format jsonl

# Multiple images as one document
light-ocr document scan1.png scan2.png scan3.png --format text
```

Programmatic API:

```ts
import { recognizeDocument } from "@arcships/light-ocr";

// Stream pages from a PDF
for await (const page of recognizeDocument("report.pdf", { dpi: 200 })) {
  console.log(page.index, page.lines.length, page.source.kind);
}

// Multiple images
for await (const page of recognizeDocument([buf1, buf2, buf3])) {
  console.log(page.index, page.lines);
}
```

## What you get

- **Local processing.** Image