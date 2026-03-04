# Latent Library

![Java](https://img.shields.io/badge/Java-21-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-3.3-6DB33F?style=for-the-badge&logo=spring&logoColor=white)
![Vue.js](https://img.shields.io/badge/Vue.js-3-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white)
![PrimeVue](https://img.shields.io/badge/PrimeVue-3-06C167?style=for-the-badge&logo=primevue&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Electron](https://img.shields.io/badge/Electron-31-47848F?style=for-the-badge&logo=electron&logoColor=white)

A robust, high-performance desktop asset manager designed specifically for the AI image generation ecosystem. It unifies metadata parsing across fragmented formats, providing **SQL-backed search**, **Smart Collections**, **live folder monitoring**, and **AI-powered interrogation** in a modern, multi-themed desktop interface.

---

## 📸 Interface

<p align="center">
  <img src="frontend/src/assets/screenshots/hero_view.png" width="800" alt="Main Browser and Metadata Sidebar">
  <br>
  <i>Unified grid gallery with instant SQLite search and dynamic metadata parsing.</i>
</p>

### Rapid Organization & Inspection

<p align="center">
  <img src="frontend/src/assets/screenshots/speed_sorter.png" width="800" alt="Speed Sorter">
  <br>
  <i><b>Speed Sorter:</b> Rapidly categorize massive generation dumps using keyboard hotkeys.</i>
</p>

<p align="center">
  <img src="frontend/src/assets/screenshots/comparator.png" width="800" alt="Image Comparator Slider">
  <br>
  <i><b>Image Comparator:</b> Pixel-peep fine details between two generations with the draggable slider.</i>
</p>

<details>
<summary><b>View More Features (Collections, Duplicate Detective & Custom Themes)</b></summary>
<br>

<p align="center">
  <img src="frontend/src/assets/screenshots/dynamic_folders.png" width="800" alt="Smart Collections">
  <br>
  <i><b>Smart Collections:</b> Create dynamic, auto-populating folders based on complex metadata filters.</i>
</p>

<p align="center">
  <img src="frontend/src/assets/screenshots/duplicate_finder.png" width="800" alt="Duplicate Finder">
  <br>
  <i><b>Duplicate Detective:</b> Identify and manage identical or similar generations across your entire library.</i>
</p>

<p align="center">
  <img src="frontend/src/assets/screenshots/custom_themes.png" width="800" alt="Custom Themes">
  <br>
  <i>Choose between Deep Neon, Clean Light, and Dark Premium themes to suit your workspace.</i>
</p>

</details>

---

## 🔐 Portable, Private & Secure

Designed for the privacy-conscious artist, this application operates on a strictly "Local-First" philosophy.

* **Standalone Desktop App:** Runs as a single `.exe` (Windows), `.AppImage` (Linux), or `.dmg` (macOS). No installer required.
* **Bundled Runtime:** Includes a self-contained Java 21 environment. No system-wide Java installation is required.
* **Portable Data:** All data (database, thumbnails, settings) is stored in a local `data/` folder next to the executable (or in a standard user data location on macOS), making it easy to backup or move.
* **100% Offline / No Telemetry:** There are no "cloud sync" features, analytics, or background API calls. Your prompts and generation data never leave your machine.
* **Privacy Scrubbing:** Integrated **Scrubber View** allows you to sanitize images before sharing. It strips hidden generation metadata (Prompts, ComfyUI Workflows, Seed data) while preserving visual quality.

---

## ✨ Key Features

* **Universal Metadata Engine:** Advanced parsing strategies for the entire stable diffusion ecosystem.
  * **ComfyUI:** Traverses complex node graphs (recursive inputs) and API formats to identify the true Sampler, Scheduler, and LoRAs used.
  * **Automatic1111 / Forge:** Robust parsing of standard "Steps: XX, Sampler: XX" text blocks.
  * **Others:** Native support for **InvokeAI**, **SwarmUI**, and **NovelAI**.
  * *Note: Metadata extraction requires images to contain embedded EXIF or PNG text chunks (standard for most AI generators).*
* **AI Auto-Tagger:** Integrated **WD14 ONNX** model for local image interrogation. Automatically generate descriptive tags for your library without external API calls.
* **Library Management:**
  * **Smart Collections:** Create dynamic collections based on metadata filters (e.g., "All images using Flux model with > 4 stars").
  * **Visual Previews:** Collections feature a 3D-stacked image preview for immediate visual context.
  * **Pinned Folders:** Bookmark frequently accessed directories for rapid navigation.
  * **Star Ratings:** Rate images (1-5 stars) with instant filtering.
* **Speed Sorting:** A dedicated mode for processing high-volume generation batches.
  * **Hotkeys:** Instantly move images to configurable target folders using numeric keys (1-5).
  * **Recycle Bin:** Safely move unwanted results to the OS trash (Recycle Bin/Trash).
