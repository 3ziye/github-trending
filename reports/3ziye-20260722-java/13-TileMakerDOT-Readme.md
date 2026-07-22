# TileMaker DOT Application

***

## 🌟 Overview

**TileMaker DOT** is a custom map creation application designed for game developers who need a **fast, efficient, and user-friendly tool**. It provides a unique, streamlined workflow and flexible asset management system, allowing you to focus purely on map design.

**Created by:** Andrei Voia

***

## 💻 Platform Support

**TileMaker DOT** is a cross-platform application. To ensure maximum performance and portability, specific versions of the Java Runtime are included for each system.

**Windows** Fully supported (x64)

**Linux** Fully supported (Ubuntu, Mint, Debian, etc.)

**macOS** Fully supported (Intel x64 & Apple Silicon via Rosetta)

***

## 📥 Download
Get the latest version of TileMaker DOT on Itch.io:
[**Download on Itch.io**](https://crytek22.itch.io/tilemakerdot)

***

## ✨ Key Features & Benefits

TileMaker DOT addresses common limitations found in traditional map editors by offering:

| Feature Category         | TileMaker DOT Benefit | Competitive Advantage |
| ---                      | ---                   | ---                   |
| **Multi-Platform**       | Native Launchers for Windows/Mac/Linux.                                                     | Runs anywhere without needing a system-wide Java installation. |
| **Personalization & UI** | **Light and Dark Themes** Optimized for long dev sessions and better visibility in different environments. | Features a modern and professional aesthetic. |
| **Export Control**       | Universal Compatibility: Supports **CSV, XML, JSON, TMX (Tiled), TMJ, and .LVL** formats.   | Provides granular control over the final file structure and appearance. |
| **Asset Management**     | Images can be modified and added later without altering the unique ID of existing textures. | Avoids "breaking" existing map data when updating visual assets. |
| **Hot-Reloading**        | Re-scans folders and updates textures without restarting.                                   | Dramatically speeds up the art pipeline by allowing "Live Edits." |
| **Animation System**     | **Frame-Based Sync** Automatically detects frames and synchronizes them globally.           | Ensures all animated world objects (torches, water) flicker in perfect unison. |
| **Auto-ID Assistant**    | **Intelligent Prefixing** Automatically assigns unique IDs to textures missing them.        | Eliminates the tedious manual task of naming files, preventing ID conflicts automatically. |
| **Chunk Selection**      | Drag-and-drop mass manipulation for copying, moving, or exporting map sections.             | Simplifies modular map design by allowing users to save and reuse "chunks" (houses, rooms). |
| **Random Brush**         | **Scatter Painting** Select multiple IDs to paint randomized variations automatically.      | Breaks up visual repetition in natural environments like forests or grasslands. |
| **Texture Organization** | Allows the user to define custom IDs for all used textures.                                 | Ensures map data aligns perfectly with your game's object structure, rather than adapting to randomly assigned editor IDs. |
| **Layer Simplicity**     | Uses a single layer for each map type (`tiles`, `objects`, `npcs`), with automatic visual depth sorting(front-to-back sorting). This sorting is determined by analyzing the object's bottom-most non-transparent pixels. | Eliminates the complex "Photoshop-style" management of multiple layers just for depth sorting. By using pixel analysis, it provides pixel-perfect visual layering without manual configuration. |
| **Dynamic Resizing**     | Provides powerful quick-action tools for map expansion and resizing.                        | Allows easy modification of the map canvas size after creation, offering flexibility for evolving project needs. |
| **User Experience**      | Reduces the learning curve and speeds up map creation for the end-user.                     | A streamlined and intuitive interface makes the application significantly easier to use than similar complex tools. |
| **Asset Filtering**      | Selective ID Loading: Only imports assets defined in a specific whitelist file.             | Prevents workspace clutter and memory overhead by excluding unused or legacy textures without needing to delete files. |
| **Spritesheet Slicer**   | Import a full sheet and cut it into individual assets without leaving the app.              | Eliminates the need for external image editors and automatically handles file saving and ID assignment in one workflow. |
| **Annotated Notes**      | Place persistent, color-coded pins directly onto map tiles to leave design memos, boundary and script reminders, or map out level design notes. | Keeps level design ideas, collaboration notes, and scripting instructions attached directly to the map canvas, scaling perfectly during meetings and game development. |
***

***

## 🎮 Game Engine Compatibility

TileMaker DOT provides multiple export options to