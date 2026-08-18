<div align="center">
  <h1>doc7</h1>
  <p><strong>Any document in. AI-ready Markdown out.</strong></p>
  <p>Turn PDFs, Office files, scans, screenshots, charts, formulas, and diagrams into Markdown your AI can search, quote, and reason over.</p>
  <p><a href="./README.zh-CN.md">简体中文</a> · English</p>
  <p><a href="https://github.com/magicrew/doc7">GitHub</a> · <a href="https://github.com/magicrew/doc7/releases">Releases</a> · <a href="./benchmarks/attention-is-all-you-need/README.md">Benchmark</a></p>
</div>

[![Build](https://github.com/magicrew/doc7/actions/workflows/build.yml/badge.svg)](https://github.com/magicrew/doc7/actions/workflows/build.yml) [![Latest Release](https://img.shields.io/github/v/release/magicrew/doc7?display_name=tag)](https://github.com/magicrew/doc7/releases) [![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

[![doc7 turns any document into AI-ready Markdown](./assets/readme/hero/hero.webp)](#quick-start)

`doc7` turns PDFs, Office files, scans, screenshots, charts, formulas, and
diagrams into Markdown through your own OpenAI-compatible multimodal model.
No required OCR stack. No document-processing service lock-in.

## Quick Start

Install doc7, start a local vision model in LM Studio or Ollama, then convert a
document:

```bash
# macOS or Linux
curl -fsSL https://raw.githubusercontent.com/magicrew/doc7/main/scripts/install.sh | bash

# Windows PowerShell
irm https://raw.githubusercontent.com/magicrew/doc7/main/scripts/install.ps1 | iex

# Convert a document
doc7 report.pdf
```

The first run discovers the local model endpoint and saves the selected model
on this machine. For a remote endpoint, configure it with `doc7 setup`.

## Understand Complex Pages

[![doc7 turns Attention Is All You Need into AI-ready Markdown](./examples/attention-is-all-you-need/showcase.webp)](./examples/attention-is-all-you-need/input.webp)

One raster-only page from *Attention Is All You Need*. No text layer. doc7
recovers the paper identity, Figure 2, the displayed equation, the scaling
rationale, the technical footnote, and the ordered relationships inside both
attention diagrams as searchable Markdown.

The same pipeline processes complete papers and multi-page reports, then
rebuilds the ordered pages into one document.

`doc7` reads the whole page instead of stopping at character extraction. Bring
any OpenAI-compatible multimodal model, including a private or local deployment.
There is no required OCR stack and no per-page document-parser fee from doc7.

## Measured on Real Inputs

[![doc7 Visual Understanding Benchmark](./assets/readme/benchmark/benchmark.webp)](./benchmarks/visual-report/README.md)

Two raster-only PDFs. Fifteen machine-checkable visual facts. MarkItDown OCR
and doc7 used the same `qwen3.5-9b` model through the same local
OpenAI-compatible endpoint. Docling used its standard local pipeline.

In this run, doc7 recovered **15/15** checked facts, compared with 9/15 for
MarkItDown with its OCR plugin and 3/15 for Docling's standard pipeline.

## One Pipeline for Every Format

[![doc7 processes every document through one visual-understanding pipeline](./assets/readme/formats/formats.webp)](#supported-inputs)

Different containers enter the same page-understanding pipeline. Text, tables,
formulas, charts, diagram relationships, image meaning, and visible UI state
leave as one searchable Markdown document.

## Built Around the CLI

[![doc7 command-line interface on macOS, Linux, and Windows](./assets/readme/cli/cli.webp)](#quick-start)

The same binary provides the interactive CLI, batch processing, model checks,
MCP, the Go SDK, and the asynchronous HTTP service.

## Detailed Setup and Usage

**Download:** [macOS, Linux, and Windows CLI archives](https://github.com/magicrew/doc7/releases)

Install the latest release without administrator privileges.

macOS or Linux:

```bash
curl -fsSL https://raw.githubusercontent.com/magicrew/doc7/main/scripts/install.sh | bash
```

Windows PowerShell:

```powershell
irm https://raw.githubusercontent.com/magicrew/doc7/main/scripts/install.ps1 | iex
```

The installer is the recommended macOS path. It downloads a checksum-verified
release and installs it under your user directory, so it does not require an
administrator account or an Apple Developer ID. Directly opening a binary
downloaded by a browser is different: macOS may attach a quarantine attribute
to that file. If you choose the archive path, run the included command from
Terminal after extracting it:

```bash
xattr -dr com.apple.quarantine <extracted-directory>
```

This removes the local download quarantine; it is not Apple signing or
notarization. Official Developer ID signing and notarization require an Apple
Developer Program account and are planned for a future signed release channel.

Start LM Studio or Ollama, load a local vision model, and convert a file:

```bash
doc7 report.pdf
doc7 screenshot.png
```

That is the complete first-run flow. doc7 detects t