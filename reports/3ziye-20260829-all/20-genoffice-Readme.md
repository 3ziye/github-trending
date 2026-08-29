# GenOffice

**The world's first full-featured open-source AI Office suite.**

[![License: Apache-2.0](https://img.shields.io/github/license/genspark-ai/genoffice)](LICENSE)
[![Latest release](https://img.shields.io/github/v/release/genspark-ai/genoffice)](https://github.com/genspark-ai/genoffice/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/genspark-ai/genoffice/total)](https://github.com/genspark-ai/genoffice/releases)

[Website](https://genoffice.ai/) · [Download](https://github.com/genspark-ai/genoffice/releases/latest) · [Privacy](PRIVACY.md) · [Demo](https://www.youtube.com/watch?v=B2pLdMX95v4)

GenOffice is a free, open-source alternative to Microsoft Office for macOS,
Windows, and Linux, built around AI editing as a first-class workflow rather
than a bolted-on chat box. It opens and saves the real Microsoft Office
formats — Word (`.docx`), Excel (`.xlsx`), PowerPoint (`.pptx`) — and edits
PDF and Markdown too: a word processor, spreadsheet, presentation editor,
PDF editor, and Markdown editor as six Electron apps sharing one engine
layer.

[![Meet GenOffice — the world's first full-featured open-source AI Office (video)](https://img.youtube.com/vi/B2pLdMX95v4/maxresdefault.jpg)](https://www.youtube.com/watch?v=B2pLdMX95v4)

[Watch the demo video on YouTube](https://www.youtube.com/watch?v=B2pLdMX95v4)

## Features

- **Real PDF editing** — retype text and edit images in the page itself, original fonts preserved.
- **Local PDF → Word / PowerPoint / Excel conversion** — turn a PDF into an editable `.docx`, `.pptx`, or `.xlsx` entirely on your machine: no cloud, no upload.
- **Scanned PDFs too** — on macOS and Windows scanned pages are read with the system OCR, so they convert to editable text.
- **Microsoft Word–compatible, byte-preserving `.docx` editing** — only what you touched changes; Word never notices.
- **Word-faithful pagination** — page breaks land where Word puts them.
- **Excel-compatible spreadsheets** — in-house engine with a Rust `.xlsx` sidecar, own charts, pivot tables, slicers.
- **PowerPoint-compatible presentations** — in-house `.pptx` engine with masters, layouts, smart guides, non-destructive crop.
- **Markdown to Word, fully local** — the same OOXML engine, no Pandoc, no cloud.
- **AI that edits documents** — block-level edits with snapshots and diffs, document-aware agents.
- **Bring your own key (BYOK)** — run the AI on your own API key: Claude, OpenAI, Gemini, DeepSeek, Kimi, GLM, Qwen, Doubao, MiniMax, Grok, Mistral, OpenRouter, or any OpenAI-compatible endpoint — or sign in with Genspark and skip keys entirely.
- **Agent tools built in** — web/image search, image generation, media analysis.
- **Light / dark / system themes.**
- **macOS, Windows, Linux.**
- **Free & open-source (Apache-2.0).**

## Download

| Platform                             | Requirements                                          | Download                                                                            |
| ------------------------------------ | ----------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **macOS** — Apple Silicon (arm64)    | macOS 11+                                             | [Latest `.dmg` (arm64)](https://github.com/genspark-ai/genoffice/releases/latest)   |
| **macOS** — Intel (x64)              | macOS 11+                                             | [Latest `.dmg` (x64)](https://github.com/genspark-ai/genoffice/releases/latest)     |
| **Windows** (x64)                    | Windows 10+                                           | [Latest `.exe` installer](https://github.com/genspark-ai/genoffice/releases/latest) |
| **Linux** — Debian / Ubuntu          | x86_64, glibc 2.34+ (Ubuntu 22.04 or newer)           | [Latest `.deb`](https://github.com/genspark-ai/genoffice/releases/latest)           |
| **Linux** — Fedora / RHEL / openSUSE | x86_64, glibc 2.34+ (Fedora 35+, RHEL 9+, Leap 15.6+) | [Latest `.rpm`](https://github.com/genspark-ai/genoffice/releases/latest)           |
| **Linux** — other distributions      | x86_64, glibc 2.34+, FUSE 2                           | [Latest `.AppImage`](https://github.com/genspark-ai/genoffice/releases/latest)      |

All builds come from `main`; the macOS and Windows installers are signed.
Older versions are on the [Releases](https://github.com/genspark-ai/genoffice/releases) page.

### Installing on Linux

The deb installs with apt — it pulls in the dependencies and adds GenOffice
to the applications menu:

```bash
sudo apt install ./genoffice_<version>_amd64.deb
```

On Fedora / RHEL-family / openSUSE, install the rpm instead:

```bash
sudo dnf install ./genoffice-<version>.x86_64.rpm     # Fedora / RHEL family
sudo zypper install ./genoffice-<version>.x86_64.rpm  # openSUSE
```

The AppImage instead runs in place: install the FUSE 2 runtime
(`sudo apt install libfuse2`; on Ubuntu 24.04 the package is `libfuse2t64`),
make