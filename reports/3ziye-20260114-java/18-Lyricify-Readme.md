# 🎵 Lyricify

<div align="center">

![Lyricify Banner](screenshots/mainActivity.jpg)

**A powerful Android lyrics application with real-time synced lyrics, multiple rendering engines, and advanced tag editing**

[![Android](https://img.shields.io/badge/Platform-Android-green.svg)](https://www.android.com/)
[![API](https://img.shields.io/badge/API-29%2B-brightgreen.svg)](https://android-arsenal.com/api?level=29)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

[Features](#features) • [Screenshots](#screenshots) • [Installation](#installation) • [Usage](#usage) • [Building](#building) • [Contributing](#contributing)

</div>

---

## ✨ Features

### 🎤 Advanced Lyrics Display
- **Multiple Format Support**: LRC, ELRC (Enhanced LRC), ELRC Multi-Person, LRC Multi-Person, TTML
- **Real-time Synchronization**: Word-by-word highlighting with dynamic glow effects
- **Three Rendering Engines**:
  - **Native Engine**: Custom Android view with optimized rendering
  - **Karaoke/Accompanist Engine**: Specialized karaoke-style display
- **Smart Animation**: Speed-adaptive glow effects that adjust based on lyric timing
- **Interactive Seeking**: Tap any line to jump to that timestamp

### 🎨 Customization
- **6 Font Styles**: Default, Serif, Sans Serif, Monospace, Cursive, Casual
- **Immersive Mode**: Full-screen lyrics experience with gesture controls
- **Squiggly Seekbar**: Animated, wave-based progress indicator with liquid effects
- **Layout Options**: Traditional top-based or modern bottom-based UI
- **Background Blur**: Native Android 12+ blur with fallback for older versions

### 🎵 Media Integration
- **Universal Player Support**: Works with any music player via Media Session API
- **Now Playing Detection**: Automatic artwork and metadata extraction
- **Playback Controls**: Play, pause, skip, and seek from within the app
- **Real-time Sync**: 60 FPS smooth scrolling and animation

### 🏷️ Tag Editor
- **Comprehensive Metadata Editing**: Title, Artist, Album, Genre, Year, Composer, and more
- **Artwork Management**:
  - Support for static images (JPEG, PNG)
  - **Animated artwork** support (GIF, WebP)
  - **Motion artwork** via Lyricify Companion app (video to image conversion)
  - Artwork resizing with quality presets
- **Lyrics Embedding**: Embed synced lyrics directly into audio files
- **Custom Fields**: Add any custom metadata tags
- **Batch Operations**: Save as .lrc/.ttml files alongside audio

### 📁 Library Management
- **Smart Filtering**:
  - Hide songs with embedded lyrics
  - Hide songs with external .lrc files
  - Folder whitelisting/blacklisting
- **Advanced Search**: Real-time search across title and artist
- **Multiple Sort Options**: By Title, Artist, or Date Added (ascending/descending)
- **Fast Scrolling**: Optimized RecyclerView with section headers

### 🚀 Performance Features
- **Background Caching**: Pre-loads lyrics for faster access
- **Low RAM Mode**: Optimized memory usage for older devices
- **Smart Image Loading**: Glide-based caching with animated artwork support
- **Scroll Optimization**: Flinging mode for smooth list performance

### 🔧 Advanced Features
- **Metadata API Integration**: Automatic song identification and metadata fetching
- **Offline Support**: Works with locally stored music files
- **Permission Management**: Smart storage permission handling for Android 11+
- **File Detection**: Automatic .lrc file detection for hiding feature
- **Update Checker**: Built-in update notification system

---

## 📸 Screenshots

<div align="center">

| Main Library | Lyrics View | Tag Editor |
|:---:|:---:|:---:|
| ![Main](screenshots/mainActivity.jpg) | ![Lyrics](screenshots/lyrics.jpg) | ![Tags](screenshots/tagEditor.jpg) |

| Player Screen | Immersive Mode | Settings |
|:---:|:---:|:---:|
| ![Player](screenshots/player.jpg) | ![Immersive](screenshots/immersive.jpg) | ![Settings](screenshots/settings.jpg) |

| Sort Dialog | Now Playing |
|:---:|:---:|
| ![Sort](screenshots/sortDialog.jpg) | ![MainActivity2](screenshots/mainActivity2.jpg) |

</div>

---

## 📦 Installation

### Requirements
- Android 10 (API 29) or higher
- Storage permissions for accessing music files
- Notification access for media session integration
- (Optional) MANAGE_ALL_FILES permission for .lrc file detection

### Download
1. Download the latest APK from the [Releases](https://github.com/amanrajaryan/lyricify/releases) page
2. Enable "Install from Unknown Sources" in your device settings
3. Install the APK
4. Grant required permissions when prompted

---

## 🎯 Usage

### First Launch
1. **Grant Storage Permission**: Allow access to your music library
2. **Grant Notification Access**: Enable media detection for Now Playing
3. **Library Scan**: The app will automatically scan your music files

### Getting Lyrics
1. **Tap a song** in your library
2. The app will attempt to identify the song and fetch lyrics
3. If identification fails, you can manually search
4. **Choose format**: Plain, LRC, ELRC, TT