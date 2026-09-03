<p align="center">
  <img src="assets/hero.svg" width="100%" alt="DSH Vision Router — eyes for text-only DeepSeek Harness agents" />
</p>

<h1 align="center">dsh-vision-router</h1>

<p align="center"><strong>Turn vision on when you need it — eyes for text-only agents on DeepSeek Harness. Free out of the box, no key, no Python, one command.</strong></p>

<p align="center">DeepSeek keeps thinking; the built-in free vision chain and fourteen deep tools do the seeing. When an image matters, enable the composer’s “👁 Vision” control and use image turns like ordinary tool-calling turns — grounded, measurable, repeatable.</p>

<p align="center">
  <a href="https://awesome-dsh-plugin.com"><img src="https://awesome-dsh-plugin.com/badge.svg" alt="awesome · DSH plugin" /></a>
  <a href="https://github.com/zp-home/dsh-recommend"><img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fzp-home%2Fdsh-recommend%2Fmain%2Fdata%2Fbadges%2Fysr666__dsh-vision-router.certified.json&amp;style=flat-square" alt="dsh-recommend 🏅 certified" /></a>
  <a href="https://www.dshbase.com/plugins/dsh-vision-router/"><img src="https://img.shields.io/badge/dshbase-install--tested-2EA44F?style=flat-square" alt="dshbase install-tested" /></a>
  <a href="https://github.com/SoberReport-AI/DeepGuard/blob/main/reports/dsh-vision-router/2.0.1/39c8f2b2d69aa398418fd6c8ab40b691a92a1a3d.json"><img src="https://img.shields.io/badge/DeepGuard-audit%20clean-2EA44F?style=flat-square" alt="DeepGuard audit clean" /></a>
  <a href="https://whyihaveyou.github.io/dsh-suite/"><img src="https://img.shields.io/badge/featured%20on-dsh--suite-4d6bfe?style=flat-square" alt="featured on dsh-suite" /></a>
</p>

<p align="center">
  <a href="https://github.com/ysr666/dsh-vision-router/releases/tag/v2.1.0"><img src="https://img.shields.io/badge/release-v2.1.0-5B4CF0?style=flat-square" alt="Release v2.1.0" /></a>
  <a href="tests"><img src="https://img.shields.io/badge/verified-Node%2022%20%2B%2024-2EA44F?style=flat-square" alt="Verified: Node 22 + 24" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-2EA44F?style=flat-square" alt="License: MIT" /></a>
  <a href="package.json"><img src="https://img.shields.io/badge/Node.js-%3E%3D22-339933?style=flat-square&amp;logo=nodedotjs&amp;logoColor=white" alt="Node.js >=22" /></a>
  <img src="https://img.shields.io/badge/runtime-no%20Python-8A2BE2?style=flat-square" alt="No Python" />
</p>

<p align="center">
  <sub>Ecosystem:</sub>
  <a href="https://dshplugin.app/plugins/dsh-vision-router">DSHPlugin.app</a> ·
  <a href="https://github.com/diegosouzapw/awesome-omni-dsh-plugins">Awesome Omni DSH Plugins</a> ·
  <a href="https://dshpluginhub.ai/plugins/dsh-vision-router">dshpluginhub.ai</a> ·
  <a href="https://www.dsh.plus/en/plugins/dsh-vision-router/">dsh.plus</a> ·
  <a href="https://dshplugins.ai/">dshplugins.ai</a> ·
  <a href="https://dshmarket.com/p/ysr666/dsh-vision-router/">dsh-market</a>
</p>

<p align="center">English · <a href="README.zh.md">中文</a></p>

<p align="center">💬 <strong>QQ community group: 1105463028</strong></p>

> [!WARNING]
> 📌 **Announcement (v2.1.0)**
>
> **v2.1.0:** Native five-card Settings, explicit Vision mode, runtime i18n, hardened capability routing/benchmarks, and the DSH rc.8 support floor. [What’s new →](docs/releases/v2.1.0.md)

<p align="center">
  <img src="assets/vision-demo.gif" width="640" alt="Demo: paste an image, the agent locates the send button with vision_ground / vision_crop / vision_pixel_diff and answers with coordinates" />
</p>

## Contents

- [Why this exists](#why-this-exists)
- [How it compares](#how-it-compares)
- [Design lineage](#design-lineage)
- [Acknowledgements](#acknowledgements)
- [Quick start](#quick-start)
- [Free vision key channels](#free-vision-key-channels)
- [Highlights](#highlights)
- [How it works](#how-it-works)
- [Tools](#tools)
- [Configuration](#configuration)
- [Install and lifecycle](#install-and-lifecycle)
- [Troubleshooting](#troubleshooting)

## Why this exists

Most DSH vision plugins bridge images to DeepSeek as *text descriptions* — lossy, one-shot, and blind to pixels. This plugin keeps the **Host-canonical image pixels on the vision model's side** and DeepSeek on the reasoning side, and makes looking at an image an **ordinary tool call**:

- **One command install.** The package ships its own composition patch (`dsh.bundle.patch`): `dsh plugin add` wires the row, the admission wrapper and the attachment limits automatically — zero manual file edits. Taking over the official DeepSeek route is an optional setting (stealth mode, off by default).
- **Free by default.** Vision tools end with a five-model OVHcloud anonymous fallback: no account, no key, 2 requests/minute per IP per model, roughly 10 RPM in theory across independent buckets. User-provided vision models run first.
- **No Python.** The whole pipeline — downscale, grounding, crop, pixel diff, palette, OCR, SVG trace, cutout, HTML 