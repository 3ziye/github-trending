# NoteLite

<div align="center">

**An OMR-based platform for lightweight score structuring, error detection, and music-education evaluation**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/badge/release-v5.11.0-brightgreen.svg)](https://github.com/Lucas0623z/NoteLite/releases/latest)
[![Status](https://img.shields.io/badge/status-In%20Development-yellow.svg)]()
[![GitHub](https://img.shields.io/badge/GitHub-Lucas0623z-blue?logo=github)](https://github.com/Lucas0623z)

[Features](#features) • [Architecture](#architecture) • [Installation](#installation) • [Roadmap](#roadmap) • [Contact](#contact)

</div>

---

## Overview

NoteLite is a smart score-processing platform aimed at music-education scenarios. Built on Optical Music Recognition (OMR), combined with lightweight encoding, score matching, and error detection, it forms a complete loop from "scan recognition" to "database management" to "teaching feedback".

### Background & Motivation

Existing OMR tools (Audiveris, oemer, homr, etc.) can already convert score images into machine-readable formats such as MusicXML, but several gaps remain for real music-education platforms:

- No lightweight structured representation suitable for database storage
- No automatic matching and diffing against canonical scores
- No suspected-error detection on scanned scores
- No audio-based assessment of performance correctness

NoteLite is designed to fill these gaps. **It is not another OMR engine** — it builds an education-oriented application layer on top of mature open-source OMR.

---

## Latest Release (v5.11.0, 2026-04-29)

NoteLite is currently a fork of the Audiveris OMR engine. The released desktop build includes:

- **Full OMR pipeline**: PDF / image → transcription → MusicXML export
- **MIDI export** (new in this release): file-type dropdown supports `.mxl` / `.xml` / `.mid`, with no need for MuseScore or other external tools
- **Chinese UI**: full zh_CN localization of menus / dialogs / toolbars
- **JDK 21 build**: extract and run, no compilation needed

Download: [`NoteLite-5.11.0.zip`](https://github.com/Lucas0623z/NoteLite/releases/latest)

> MIDI export is intended for proof-listening only. The first version uses a fixed velocity of 80; advanced features such as drum kits, repeat marks, and transposing instruments are not yet supported. See the release notes for details.

---

## Features

### Core Modules

| Module | Description | Status |
|--------|-------------|--------|
| **Score Recognition** | Recognize scanned, photographed, and PDF scores | In progress |
| **Lightweight Encoding** | Convert scores into compact structured data optimized for storage and retrieval | In progress |
| **Score Matching** | Auto-match against canonical scores with sequence-level diffing | Planned |
| **Smart Correction** | Detect missing/wrong notes, rhythm anomalies, accidental errors, etc. | Planned |
| **Performance Assessment** | Coarse-grained performance evaluation based on audio recognition | Planned |

### Highlights

1. **Lightweight score encoding**
   A compressed representation designed for databases — far smaller than full MusicXML.

2. **Canonical-score-driven diffing**
   New scans are not just recognized; they are also automatically validated against the canonical version in the database.

3. **Education-oriented closed loop**
   An end-to-end flow from paper score to online teaching feedback.

---

## Architecture

### System Layers

```
┌─────────────────────────────────────────────────┐
│                Application Layer                 │
│   Upload | Matching | Correction | Assessment   │
└─────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────┐
│            Database & Retrieval Layer           │
│   Canonical | User Uploads | Versions | Index   │
└─────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────┐
│              Lightweight Encoding               │
│   Relative pitch | Tokenize | Hash | Compress   │
└─────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────┐
│             Score Structuring Layer             │
│  Clef | Key | Time | Notes | Duration | Marks   │
└─────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────┐
│               OMR Recognition Layer             │
│  Preprocess | Staff detection | Symbols | Pitch │
└─────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────┐
│                   Input Layer                   │
│   Scanned image | Photo | PDF | Audio recording │
└─────────────────────────────────────────────────┘
```

### Tech Stack

- **OMR engine**: Audiveris / oemer / homr (alternative options)
- **Data forma