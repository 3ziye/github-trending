<div align="center">

![Lokus Logo](assets/lokus-logo.svg)

# Lokus

**A lightning-fast, privacy-first knowledge management system built with Tauri and React**

*Why settle for 10+ plugins when you can have everything built-in?*

[![GitHub Stars](https://img.shields.io/github/stars/lokus-ai/lokus?style=social)](https://github.com/lokus-ai/lokus/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Discord](https://img.shields.io/badge/Discord-Join%20Us-7289DA?logo=discord&logoColor=white)](https://discord.gg/lokus)

[🚀 Quick Start](#-quick-start) • [✨ Features](#-features) • [📸 Screenshots](#-screenshots) • [🗺️ Roadmap](#️-roadmap) • [🤝 Contributing](#-contributing)

</div>

---

## 🎯 Why Lokus?

Built by an Obsidian user who got tired of plugin dependencies. Lokus gives you **everything you need out of the box**:

| Obsidian | Lokus |
|----------|-------|
| ❌ Requires Dataview plugin | ✅ Built-in database views |
| ❌ Basic graph view | ✅ 2D/3D interactive graphs |
| ❌ Canvas via plugin | ✅ Infinite canvas built-in |
| ❌ $10/month for sync | ✅ Free sync via your cloud |
| ⚡ ~100MB download | ⚡ ~10MB download |
| 🐌 Electron-based | 🚀 Rust-powered (Tauri) |

---

## 📸 Screenshots

<div align="center">

### 📝 Rich Markdown Editor with Real-time Preview
![Editor View](assets/screenshots/screenshot-1.png)

### 🕸️ 3D Knowledge Graph Visualization
![Graph View](assets/screenshots/screenshot-2.png)

### 📊 Bases - Notion-like Database Views
![Bases Database](assets/screenshots/screenshot-3.png)

### 🎨 Interactive Graph Navigation
![Graph View 2](assets/screenshots/screenshot-4.png)

### ✍️ Advanced Markdown Editing
![Markdown Editing](assets/screenshots/screenshot-5.png)

</div>

---

## ✨ Features

### 📝 **Core Writing**
- **Rich Markdown Editor** - Full GitHub Flavored Markdown support
- **Wiki Links** - Bidirectional linking with `[[Note Name]]` syntax
- **LaTeX Math** - Inline `$x^2$` and block `$$E=mc^2$$` equations
- **Code Blocks** - Syntax highlighting for 100+ languages
- **Tables** - Sortable, resizable tables with CSV export
- **Task Lists** - `- [ ]` checkbox support with progress tracking

### 📊 **Database Views (Bases)**
- **Notion-like Tables** - Sort, filter, and group your notes
- **Multiple Views** - Table, Gallery, Calendar (coming soon)
- **Custom Properties** - Add metadata without frontmatter
- **Smart Filters** - Query notes by tags, dates, properties
- **Auto-create** - Default "All Notes" base on first use

### 🕸️ **Knowledge Graph**
- **2D & 3D Graphs** - Toggle between flat and spatial views
- **Interactive Navigation** - Click nodes to open notes
- **Link Strength** - Visual weight based on connections
- **Filter by Tags** - Focus on specific topics
- **Export** - Save graph as PNG/SVG

### 🎨 **Customization**
- **Theme Editor** - Real-time theme customization
- **Dark/Light Mode** - With custom color schemes
- **Font Control** - Choose your preferred fonts
- **Layout Options** - Sidebar positions, panel sizes

### 📧 **Gmail Integration**
- **Import Emails** - Save emails as markdown notes
- **Send from Notes** - Compose emails in markdown
- **Attachment Support** - Keep email attachments
- **Thread Tracking** - Maintain email context

### 🚀 **Performance**
- **Rust Backend** - Native performance with Tauri
- **Instant Search** - Fast full-text search
- **Small Footprint** - ~10MB vs Obsidian's ~100MB
- **Quick Launch** - Sub-second startup time
- **Local-First** - All data stays on your device

### 🔌 **Extensibility**
- **Plugin System** - VS Code-like extension API
- **Hot Reload** - Develop plugins without restart
- **Custom Commands** - Add keyboard shortcuts
- **Editor Extensions** - Create custom markdown syntax

---

## 🚀 Quick Start

### 📦 Download Pre-built Binaries

**macOS** (Apple Silicon & Intel)
```bash
# Download latest .dmg from releases
# Or install via Homebrew (coming soon)
```

**Windows**
```bash
# Download installer from releases
# Portable version available
```

**Linux**
```bash
# AppImage (universal)
wget https://github.com/lokus-ai/lokus/releases/latest/download/lokus.AppImage
chmod +x lokus.AppImage
./lokus.AppImage

# Flatpak (coming soon)
```

### 🛠️ Build from Source

**Prerequisites**
- [Node.js](https://nodejs.org/) v18+
- [Rust](https://rustup.rs/) (latest stable)

```bash
# Clone the repository
git clone https://github.com/lokus-ai/lokus.git
cd lokus

# Install dependencies
npm install

# Run in development mode
npm run tauri dev

# Build for production
npm run tauri build
```

---

## 🗺️ Roadmap

### ✅ **v1.0 - Current** (Released)
- [x] Rich markdown editor
- [x] Wiki links & backlinks
- [x] 2D/3D knowledge graph
- [x] Database views (Bases)
- [x] Theme customization
- [x] Gmail integration
- [x] Plugin system

### 🚧 **v1.1 - Next** (In Progress)
- [ ] Mobile apps (iOS & Android)
- [ ] Calendar 