<p align="center">
  <img src="docs/social-preview.png" alt="Gander: take a gander at any file. Open source Android file viewer for PDF, DOCX, XLSX, PPTX, JPG, MP4, MP3 and Markdown. 100% offline, 8 MB APK, zero permissions, no ads or trackers.">
</p>

# Gander 🪿

**Take a gander at any file.** A tiny, open source, fully offline **file viewer for Android** that opens
PDF, Word (`.docx`), Excel, PowerPoint (`.pptx`), photos, videos, audio, Markdown, text and code
in one app, with **zero permissions, no ads, no tracking and no internet access at all**.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/mokshablr/gander)](../../releases/latest)
[![Build](https://img.shields.io/github/actions/workflow/status/mokshablr/gander/build.yml?branch=main)](../../actions)
![Min API](https://img.shields.io/badge/minSdk-26%20(Android%208)-brightgreen)
![Kotlin](https://img.shields.io/badge/Kotlin-100%25-purple)

Every phone ships with a dozen half-viewers that bounce your documents to cloud services.
Gander is the opposite: one small APK (about 8 MB) that renders everything **on the device**.
It cannot phone home because it does not even hold the INTERNET permission.

<p align="center">
  <img src="docs/demo.gif" width="300" alt="Gander demo: thumbnail recents, folder browsing, PDF, Word, Excel and Markdown viewing">
</p>

## Screenshots

| Home: recents and folders | Folder browsing | PDF |
| :---: | :---: | :---: |
| ![Recent files with thumbnail previews and granted folders](docs/screenshots/home.png) | ![Browsing a granted folder with previews](docs/screenshots/folder.png) | ![PDF viewer](docs/screenshots/pdf.png) |

| Word (.docx) | PowerPoint (.pptx) | Excel (.xlsx) |
| :---: | :---: | :---: |
| ![Word document viewer](docs/screenshots/docx.png) | ![PowerPoint slides viewer](docs/screenshots/pptx.png) | ![Excel spreadsheet viewer with sheet tabs](docs/screenshots/xlsx.png) |

## Features

- **One viewer for everything**: documents, spreadsheets, slides, images, video, audio, Markdown, code
- **Pinch zoom and smooth scrolling** everywhere, with deep zoom into huge photos (tiled decoding)
- **Recent files** with thumbnail previews (image, video frame, PDF first page)
- **Folder browsing** through one-time system grants, still without any storage permission
- **Share sheet and "Open with" integration**: share a file from any app (chat, mail, browser) into Gander, or tap it in a file manager
- **Find in document**: search inside Word, Excel, slides, Markdown, text and code with match navigation
- **Share and locate**: send the open file to any app, or jump to its folder in the file manager
- **Private by construction**: no permissions, no INTERNET, no analytics, no accounts, nothing leaves the phone
- **Modern Android**: Material 3, dark mode, edge to edge, works on Android 8.0+

## Supported formats

| Category | Formats | Renderer |
| --- | --- | --- |
| Documents | PDF | pdf.js, offline in a sandboxed WebView |
| | Word `.docx` | docx-preview, offline in a sandboxed WebView |
| Spreadsheets | `.xlsx` `.xls` `.xlsm` `.xlsb` `.csv` `.ods` | SheetJS, offline |
| Slides | PowerPoint `.pptx` | PPTXjs, offline |
| Photos | JPG, PNG, WebP, BMP, HEIC/HEIF | Tiled deep-zoom image view, EXIF aware |
| | GIF (animated), SVG, AVIF, ICO | WebView |
| Video | MP4, M4V, MOV, MKV, WebM, 3GP, AVI, FLV, MPEG-TS | Media3 ExoPlayer |
| Audio | MP3, M4A, AAC, FLAC, WAV, OGG, Opus, AMR | Media3 ExoPlayer |
| Markdown | `.md` rendered as formatted HTML | marked + DOMPurify, offline |
| Text and code | `.txt` `.json` `.xml` logs, most source files | Text viewer |

Anything else, including files with no extension at all, offers **View as text**, which
shows the raw contents without renaming the file. Large files load 5 MB at a time with a
**Show more** button, so they open instantly and can still be read end to end.

Legacy binary `.doc` and `.ppt` are not supported (no faithful offline renderer exists);
the app explains this and suggests re-saving as `.docx` / `.pptx`. Binary `.xls` works.

## Install

Runs on **Android 8.0 (API 26) and up**.

Viewing PDFs also needs Android System WebView 125 or newer (May 2024). Any phone
still receiving WebView updates is well past that; if yours is not, Gander says so
when you open a PDF rather than failing quietly.

1. Download the latest APK from [Releases](../../releases/latest):
   `Gander-x.y.apk` runs on every architecture, since the app ships no native code.
2. Copy it to your phone, tap it, and allow "install unknown apps" when asked.
3. Optional: Play Protect may warn about an unknown developer; that is what
   sideloaded open source looks like. Tap "Install anyway".

Updating: install the new APK over the old one; recents and folder grants survive.

**Automatic updates without a store**: install
[Obtainium](https://github.com/ImranR98/Obtainium) and add
`https://github.com/mokshablr/gander` as an app source. It fol