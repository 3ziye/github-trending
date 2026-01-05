# jdrummer

An open-source drum machine VST3 plugin built with the JUCE framework. JDrummer features Soundfont-based drum kits, a comprehensive groove library with tempo-synced playback, a composition tool, and an intelligent Groove Matcher that analyzes audio to find matching drum patterns.

![JDrummer](https://img.shields.io/badge/Format-VST3%20%7C%20AU-blue) ![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-green) ![License](https://img.shields.io/badge/License-Open%20Source-orange)

Youtube overview: https://youtu.be/mbGQnUJ8rxg?si=QsWpq8BCVJYmjcz9

## Table of Contents

- [Features](#features)
  - [Drum Pads](#-drum-pads)
  - [Grooves Browser](#-grooves-browser)
  - [Composer](#-composer)
  - [Groove Matcher](#-groove-matcher)
  - [Screenshots](#Screenshots)
- [Installation](#installation)
  - [Linux](#linux)
  - [Windows](#windows)
  - [macOS](#macos)
  - [Adding Custom SoundFonts](#adding-custom-soundfonts)
  - [Adding Custom Grooves](#adding-custom-grooves)
- [Building from Source](#building-from-source)
  - [Prerequisites](#prerequisites)
  - [Building on Linux](#building-on-linux)
  - [Building on Windows (Native)](#building-on-windows-native)
  - [Building on macOS](#building-on-macos)
  - [Cross-Compiling for Windows from Linux](#cross-compiling-for-windows-from-linux)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Tested DAWs/Known Issues](#tested-dawsknown-issues)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

### 🥁 Drum Pads
- **16-pad drum grid** with velocity-sensitive playback
- **Multiple Soundfont kits** - Ships with 28 drum kits including:
  - Standard acoustic kits (Standard, Room Drums, Power Drums, Jazz Drums)
  - Electronic kits (808, Electronic Drums, Dance Drums, House Kit)
  - Specialty kits (Orchestral Percussion, Brush Drums, NIN Drumkit)
- **Per-pad controls**:
  - Individual volume adjustment (0-100%)
- Pan control (left/right) (Panning is currently backwards, see issue 10: https://github.com/jmantra/jdrummer/issues/10 )
- Solo and mute options
- **Dynamic kit loading** - Add your own .sf2 SoundFont files to expand your library
- **Multi Out Support** - Fan each drum pience to an individual track for mixing


### 🎵 Grooves Browser
- **Extensive groove library** organized by category:
  - Basic Beats
  - Break Beats
  - Buildups
  - Double Bass Beats
  - Fills
  - Half Time Beats
  - OffBeats
  - Swing Beats
  - Tom Beats
- **Tempo-synced playback** - Grooves automatically sync to your DAW's tempo
- **Preview functionality** - Audition grooves before adding them to your project
- **Drag and drop** - Drag any groove directly into your DAW as a MIDI clip
- **Bar selection** - Choose how many bars of a groove to use (1-16 bars)
- **Dynamic Groove Loading** add your own drum grooves

### 🎼 Composer
- **Build complete drum parts** by combining multiple grooves
- **Visual timeline** showing your arrangement
- **Reorder and remove** items from your composition
- **Export as MIDI** - Drag your entire composition to the DAW
- **Loop playback** for previewing your arrangement

### 🎯 Groove Matcher
An intelligent feature inspired by professional drum software that helps you find the perfect groove for your music:

- **Audio analysis** - Drop any audio file (WAV, MP3, FLAC, OGG, AIFF) to analyze its rhythm
- **BPM detection** - Automatically detects tempo using the minibpm library
- **Smart filename parsing** - Extracts BPM from filenames (e.g., "beat_120bpm.wav")
- **Pattern matching** - Analyzes rhythm patterns and finds matching grooves from your library
- **Similarity scoring** - Shows match percentage for each suggested groove
- **Preview with audio** - Play back the matched groove alongside your original audio
- **Automatic composition** - Best match is automatically added to the composer
- **Seamless workflow** - Found the perfect match? Drag it straight to your DAW

### Screenshots
Drum Kits Tab
![Screenshot](https://i.postimg.cc/BQx7FDgQ/jdrummer-kits.png)

Grooves Tab
![Screenshot](https://i.postimg.cc/9MRJQqM6/jdrummergrooves.png)

Groove Matcher Tab

![Screenshot](https://i.postimg.cc/fTj5ysw6/jdrummermmatch.png)




## Installation
Binary VST3 for Linux, Windows, and macOS available on the **[Releases](https://github.com/jmantra/jdrummer/releases)** page. macOS builds include both VST3 and Audio Unit (AU) formats.

### Linux
Copy the VST3 bundle to your VST3 directory:
```bash
cp -r jdrummer.vst3 ~/.vst3/
```

### Windows
Copy the `jdrummer.vst3` folder to one of these locations:
- **System-wide**: `C:\Program Files\Common Files\VST3\`
- **User only**: `C:\Users\<YourUsername>\Documents\VST3\`

### macOS
JDrummer builds as both **VST3** and **Audio Unit (AU)** on macOS.

**VST3 Installation:**
Copy the VST3 bundle to your VST3 directory:
```bash
cp -r jdrummer.vst3 ~/Library/Audio/Plug-Ins/VST3/
# Or system-wide:
su