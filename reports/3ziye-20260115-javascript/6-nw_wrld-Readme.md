# nw_wrld

nw_wrld is an event-driven sequencer for triggering visuals using web technologies. It enables users to scale up audiovisual compositions for prototyping, demos, exhibitions, and live performances. Users code their own visual modules, then orchestrate them using the project's native UI composer.

Visuals can be triggered via the built-in 16-step sequencer or by configuring external MIDI/OSC inputs.

![Node Version](https://img.shields.io/badge/node-%3E%3D20.0.0-brightgreen)
![Electron](https://img.shields.io/badge/electron-v39.2.7-blue)

<img width="1512" height="901" alt="Screenshot 2026-01-09 at 14 17 49" src="https://github.com/user-attachments/assets/9d59fe7d-cc3b-48ec-af11-007a9379cac5" />

## Beta Notice

This project is currently in beta. Downloadable installers are not currently provided; run `nw_wrld` from source using this repository. Please note that whilst the project is in beta, there will likely be frequent breaking changes between releases.

## Roadmap

- [x] Isolated sandbox and module-workspace bundling
- [x] Docblock-declared module dependencies with automated runtime injection
- [ ] TypeScript migration
- [ ] Signed and notarized macOS builds +
- [ ] signed Windows builds for frictionless installs
- [ ] Linux support
- [ ] Userdata and module versioning (plus migration scripts)
- [ ] Multi-band audio threshold analysis (local processing) for channel triggers
- [ ] Advanced default sequencer (Working sampler with audio FX)
- [ ] Remote API input source with HTTP/WebSocket client for cloud-based services (audio analysis APIs, ML models, etc.)
- [ ] Serial port input support for hardware sensor integration
- [ ] JSON versioning (and migration scripts)

## Features

- **Built-in 16-step pattern sequencer** - Create rhythmic audiovisual compositions without external hardware
- **External MIDI/OSC support** - Connect Ableton Live, TouchOSC, or any MIDI/OSC source for live performance
- **Visual module system** - Build custom visuals with p5.js, Three.js, D3.js, or vanilla JavaScript
- **Hot module reloading** - Edit modules and see changes instantly
- **Project folder workflow** - Self-contained, portable projects with modules, assets, and data
- **Flexible method mapping** - Trigger any visual method with sequencer patterns or external signals

---

## Installation

### For Developers

Build from source to contribute or customize:

**Prerequisites:** Node.js v20+ and basic terminal knowledge

```bash
# 1. Clone the repository
git clone https://github.com/aagentah/nw_wrld.git
cd nw_wrld

# 2. Install dependencies
npm install

# 3. Start the app
npm start
```

Two windows will open:

- **Dashboard**: Control center for creating tracks, programming patterns, and configuring visuals
- **Projector**: Visual output window

---

## Project Folders

nw_wrld uses a **project folder** model. Each project is a self-contained folder containing your modules, assets, and data.

**Note:** Workspace modules are JavaScript code executed by nw_wrld. Only open project folders you trust.

### What's Inside a Project Folder

```
MyProject/
├── modules/           # Visual modules (hot-reloadable JavaScript files)
│   ├── Text.js
│   ├── GridOverlay.js
│   ├── SpinningCube.js
│   └── ...16 starter modules
├── assets/            # Images, JSON, and other resources
│   ├── images/
│   │   └── blueprint.png
│   └── json/
│       └── meteor.json
└── nw_wrld_data/      # Tracks, settings, and recordings
    └── json/
```

### First Launch Experience

When you first launch nw_wrld, you'll be prompted to select or create a project folder. The app automatically scaffolds a working project with:

- **16 starter modules** - Ready-to-use examples (2D, 3D, text, data visualization)
- **Sample assets** - Images and JSON data files
- **Data storage** - Configuration, tracks, and recordings

### Portability

Projects are completely portable - copy the folder to share with others, work across machines, or back up your work. Everything needed to run your audiovisual compositions is contained in one folder.

### Lost Project?

If your project folder is deleted, moved, or disconnected (e.g., external drive unplugged), nw_wrld will detect the issue and prompt you to reselect or choose a different project.

---

## Quick Start

### 60-Second Test

1. Click **[CREATE TRACK]** → Name it → Create
2. Click **[+ MODULE]** → Select **Text** or **Corners**
3. Click **[+ CHANNEL]** to add a sequencer row
4. Click some cells in the 16-step grid (they turn red)
5. Assign a method to the channel (e.g., `color` or `rotate`)
6. Click **[PLAY]** in the footer

You'll see the playhead move across the grid and trigger your visuals. No external setup required!

---

## How It Works: The Big Picture

```
Signal Sources:
┌──────────────┐
│  Sequencer   │──┐
│  (Built-in)  │  │
└──────────────┘  │
                  ├──▶ Dashboard ──▶ Projector
┌──────────────┐  │    (Control)     (Visuals)
│ External     │──┘
│ MIDI/OSC     │
└──────────────┘
``