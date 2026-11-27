<h1 align="center">Quiet.md</h1>

<p align="center">
  <b>Fast, quiet notes that live on your computer.</b><br>
  A native notes app built with Rust + GPUI: real folders, Markdown that formats itself, and a whiteboard inside your notes. Free and open source.
</p>

<p align="center">
  English · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a>
</p>

<p align="center">
  <a href="https://github.com/s1dashu/quiet-md/releases/latest"><img src="https://img.shields.io/github/v/release/s1dashu/quiet-md?label=release&color=2f6feb" alt="Latest release"></a>
  <a href="https://github.com/s1dashu/quiet-md/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/s1dashu/quiet-md/ci.yml?branch=main&event=schedule&label=CI" alt="CI status"></a>
  <img src="https://img.shields.io/badge/platform-macOS%20%7C%20Windows%20%7C%20Linux-lightgrey" alt="macOS, Windows and Linux">
  <img src="https://img.shields.io/badge/built%20with-Rust%20%2B%20GPUI-dea584?logo=rust" alt="Built with Rust and GPUI">
  <a href="LICENSE"><img src="https://img.shields.io/github/license/s1dashu/quiet-md?color=green" alt="MIT license"></a>
  <img src="https://img.shields.io/badge/status-beta-orange" alt="Beta">
</p>

<p align="center">
  <a href="https://download.quiet.md/latest/quiet-md-macos-arm64.dmg"><img src="docs/images/download-macos.svg" height="56" alt="Download for macOS"></a>
  &nbsp;
  <a href="https://download.quiet.md/latest/quiet-md-windows-x64-setup.exe"><img src="docs/images/download-windows.svg" height="56" alt="Download for Windows"></a>
  &nbsp;
  <a href="https://download.quiet.md/latest/quiet-md-x86_64.AppImage"><img src="docs/images/download-linux.svg" height="56" alt="Download for Linux"></a>
</p>

<p align="center">
  <a href="https://quiet.md/?lang=en"><b>Website</b></a> ·
  <a href="#download"><b>Download</b></a> ·
  <a href="#features">Features</a> ·
  <a href="#performance">Performance</a> ·
  <a href="CONTRIBUTING.md">Contributing</a>
</p>

<p align="center">
  <img src="docs/images/readme-home.webp" width="100%" alt="Quiet.md on a pixel-art meadow: the sidebar lists folders, and the top-level folder's page shows each folder as a stack of note cards with pictures.">
</p>

> [!NOTE]
> Quiet.md is in **beta** and changing quickly. If you hit a bug or have an idea, please [open an issue](https://github.com/s1dashu/quiet-md/issues) — or better, send a pull request.

## Why Quiet.md

**📁 Your notes are just files.** No account, no cloud, and nothing goes over the network by default, apart from the optional update check, anonymous daily usage counts from the app and the `quiet` command line tool (only counts such as how often the app was opened; turn them off in Settings › General › Anonymous usage statistics), and font downloads you cause: the handwriting font for Chinese, Japanese and Korean the first time a whiteboard needs it, and a downloadable document font when you pick one. Every folder in the sidebar is a real folder on your disk, and every note is a file named after its title: `.md` for Markdown, `.xml` for rich documents. Sync them with iCloud, Git or anything you like. If you ever stop using Quiet.md, your files stay right where they are.

**⚡ Native, and fast.** The whole interface is drawn on the GPU by Rust and [GPUI](https://www.gpui.rs/). No Electron, no WebView. In a one-million-character note, typing takes about 5 ms a frame, and a 120 Hz display allows 8.3.

**✍️ Write and draw in one place.** Type `#`, `-`, `[]` or `>` and Markdown formats itself. When words are not enough, put a whiteboard right in the note. Rich notes are stored in the Feishu (Lark) DocxXML format, so pasting from Feishu or a web page keeps its structure.

## Features

### Write

<p align="center">
  <img src="docs/images/readme-write.webp" width="100%" alt="A long note open in Quiet.md, with headings, inline math and a table of ion concentrations.">
</p>

Headings, lists, to-dos, quotes, callouts, columns, tables with merged cells, code with syntax highlighting, LaTeX math, images, files and covers. Markdown shortcuts work as you type, and the `/` menu has everything else. Mention another note to link it; the other note lists its backlinks. Mermaid code blocks draw as diagrams. Data tables keep records with select, date, number, formula, lookup and link fields, in views you filter, sort and group; each cell of a Notes column is a real note. The … menu has Focus Mode, Typewriter Mode and Paragraph Focus, and View › Zoom In enlarges the text alone.

### Draw

<p align="center">
  <img src="docs/images/readme-board.webp" width="100%" alt="A board in Quiet.md: pictures and maps laid out with handwritten labels, boxes and connecting arrows.">
</p>

Boards are a whiteboard ported from Excalidraw: shapes, arrows that stay attached, freehand, text, sti