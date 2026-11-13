<h1 align="center">Quiet.md</h1>

<p align="center">
  <b>A fast, quiet, local notes app.</b><br>
  Drawn natively with Rust + GPUI. Your notes stay on your computer, stored in the Feishu (Lark) DocxXML format.
</p>

<p align="center">
  English · <a href="README.zh-CN.md">简体中文</a> · <a href="README.ja.md">日本語</a>
</p>

<p align="center">
  <a href="https://github.com/s1dashu/quiet-md/releases/latest"><img src="https://img.shields.io/github/v/release/s1dashu/quiet-md?label=release&color=2f6feb" alt="Latest release"></a>
  <a href="https://github.com/s1dashu/quiet-md/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/s1dashu/quiet-md/ci.yml?branch=main&label=CI" alt="CI status"></a>
  <img src="https://img.shields.io/badge/platform-macOS%20%7C%20Windows%20%7C%20Linux-lightgrey" alt="macOS, Windows and Linux">
  <img src="https://img.shields.io/badge/built%20with-Rust%20%2B%20GPUI-dea584?logo=rust" alt="Built with Rust and GPUI">
  <a href="LICENSE"><img src="https://img.shields.io/github/license/s1dashu/quiet-md?color=green" alt="MIT license"></a>
  <img src="https://img.shields.io/badge/status-beta-orange" alt="Beta">
</p>

<p align="center">
  <a href="https://download.quiet.md/latest/quiet-md-macos-arm64.zip"><img src="docs/images/download-macos.svg" height="56" alt="Download for macOS"></a>
  &nbsp;
  <a href="https://download.quiet.md/latest/quiet-md-windows-x64-setup.exe"><img src="docs/images/download-windows.svg" height="56" alt="Download for Windows"></a>
  &nbsp;
  <a href="https://download.quiet.md/latest/quiet-md-x86_64.AppImage"><img src="docs/images/download-linux.svg" height="56" alt="Download for Linux"></a>
</p>

<p align="center">
  <a href="https://quiet.md/?lang=en"><b>Website</b></a> ·
  <a href="#download"><b>Download</b></a> ·
  <a href="#performance">Performance</a> ·
  <a href="#features">Features</a> ·
  <a href="CONTRIBUTING.md">Contributing</a>
</p>

<p align="center">
  <img src="docs/images/home.png" width="100%" alt="The Quiet.md home screen: a document tree on the left and all notes in a grid on the right.">
</p>

> [!NOTE]
> Quiet.md is in **beta** and changing quickly. If you hit a bug or have an idea, please [open an issue](https://github.com/s1dashu/quiet-md/issues) — or better, send a pull request.

## Why Quiet.md

**⚡ Fast, the native kind of fast.** The whole interface is drawn on the GPU by Rust and [GPUI](https://www.gpui.rs/). No WebView, no Electron. In a one-million-character document, typing, deleting and scrolling all stay under 6 ms per frame at P95.

**🔒 Local-first. Your files are yours.** No account, no cloud, and nothing goes over the network by default (the optional update check aside). Your library is an ordinary folder on your computer, and each note is one XML file. Manage it with Git, iCloud or any sync tool you like; if you ever stop using Quiet.md, your files are still there.

**📝 A full rich-text editor that speaks Feishu (Lark) DocxXML.** Notes are saved in the DocxXML format used by Feishu (Lark) Docs, so copy-paste, import and export keep their structure. Headings, to-dos, tables, columns, callouts, code, math, images and attachments — the blocks you reach for when writing documents are all there.

## Download

<p align="center">
  <a href="https://download.quiet.md/latest/quiet-md-macos-arm64.zip"><img src="docs/images/download-macos.svg" height="56" alt="Download for macOS"></a>
  &nbsp;
  <a href="https://download.quiet.md/latest/quiet-md-windows-x64-setup.exe"><img src="docs/images/download-windows.svg" height="56" alt="Download for Windows"></a>
  &nbsp;
  <a href="https://download.quiet.md/latest/quiet-md-x86_64.AppImage"><img src="docs/images/download-linux.svg" height="56" alt="Download for Linux"></a>
</p>

| Platform | Package | Requirements |
|---|---|---|
| **macOS** (Apple Silicon) | [quiet-md-macos-arm64.zip](https://download.quiet.md/latest/quiet-md-macos-arm64.zip) | macOS 13 or later |
| **Windows** (x64) | [quiet-md-windows-x64-setup.exe](https://download.quiet.md/latest/quiet-md-windows-x64-setup.exe) | Windows 10 version 2004 or later |
| **Linux** (x86_64, experimental) | [quiet-md-x86_64.AppImage](https://download.quiet.md/latest/quiet-md-x86_64.AppImage) | glibc 2.35 or later (Ubuntu 22.04 and newer) |
| **macOS** (Intel) | [quiet-md-macos-x86_64.zip](https://download.quiet.md/latest/quiet-md-macos-x86_64.zip) | macOS 13 or later |

- **macOS**: unzip and drag `quiet.md.app` into Applications. The app is signed and notarized by Apple.
- **Windows**: run the installer. By default it installs for the current user only, and uninstalling never deletes your notes. If SmartScreen appears on first launch, click **More info → Run anyway**.
- **Linux** (experimental): `chmod +x quiet-md-*.AppImage` and run it; without FUSE, add `--appimage-extract-and-run`. AppImage 0.1.10 and later support in-app updates; older Linux versions need a one-time manual install. Interactive testing so far covers Om