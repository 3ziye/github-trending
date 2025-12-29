# jdrummer

A powerful, open-source drum machine VST3 plugin built with the JUCE framework. JDrummer features SoundFont-based drum kits, a comprehensive groove library with tempo-synced playback, a composition tool, and an intelligent Groove Matcher that analyzes audio to find matching drum patterns.

![JDrummer](https://img.shields.io/badge/Format-VST3-blue) ![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows-green) ![License](https://img.shields.io/badge/License-Open%20Source-orange)

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
  - [Adding Custom SoundFonts](#adding-custom-soundfonts)
  - [Adding Custom Grooves](#adding-custom-grooves)
- [Building from Source](#building-from-source)
  - [Prerequisites](#prerequisites)
  - [Building on Linux](#building-on-linux)
  - [Building on Windows (Native)](#building-on-windows-native)
  - [Cross-Compiling for Windows from Linux](#cross-compiling-for-windows-from-linux)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Tested DAWs](#tested-daws)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

### 🥁 Drum Pads
- **16-pad drum grid** with velocity-sensitive playback
- **Multiple SoundFont kits** - Ships with 29 drum kits including:
  - Standard acoustic kits (Standard, Room Drums, Power Drums, Jazz Drums)
  - Electronic kits (808, Electronic Drums, Dance Drums, House Kit)
  - Specialty kits (Orchestral Percussion, Brush Drums, NIN Drumkit)
- **Per-pad controls**:
  - Individual volume adjustment (0-100%)
- ~~Pan control (left/right)~~ _(planned for a future release, See **[Issue 2 ](https://github.com/jmantra/jdrummer/issues/2)**)_
- ~~Solo and mute options~~ _(planned for a future release, See **[Issue 2 ](https://github.com/jmantra/jdrummer/issues/2)**)_
- **Dynamic kit loading** - Add your own .sf2 SoundFont files to expand your library

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
![Screenshot](https://i.postimg.cc/qMnR82Ds/jdrummer-kits.png)

Grooves Tab
![Screenshot](https://i.postimg.cc/ZqJCY0L1/jdrummergrooves.png)

Groove Matcher Tab

![Screenshot](https://i.postimg.cc/t4BYTpmv/jdrummermmatch.png)




## Installation
Binary VST3 for Linux and Windows available on the **[Releases](https://github.com/jmantra/jdrummer/releases)** page.

### Linux
Copy the VST3 bundle to your VST3 directory:
```bash
cp -r jdrummer.vst3 ~/.vst3/
```

### Windows
Copy the `jdrummer.vst3` folder to one of these locations:
- **System-wide**: `C:\Program Files\Common Files\VST3\`
- **User only**: `C:\Users\<YourUsername>\Documents\VST3\`

### Adding Custom SoundFonts
Place additional `.sf2` SoundFont files in the plugin's soundfonts directory:
- **Linux**: `~/.vst3/jdrummer.vst3/Contents/Resources/soundfonts/`
- **Windows**: `<VST3 Location>\jdrummer.vst3\Contents\Resources\soundfonts\`

The plugin will automatically detect new SoundFonts on the next load.

### Adding Custom Grooves
Place additional `.mid` MIDI files in the plugin's Grooves directory:
- **Linux**: `~/.vst3/jdrummer.vst3/Contents/Resources/Grooves/`
- **Wi