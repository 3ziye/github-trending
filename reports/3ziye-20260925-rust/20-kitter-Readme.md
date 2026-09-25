<p align="center">
  <img src="./assets/readme/hero.en.png" width="100%" alt="Kitter — one skill library where every project gets only what it needs">
</p>

<p align="center">
  <a href="./README.zh-CN.md">简体中文</a>
</p>

<p align="center">
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-3f8997" alt="Apache-2.0 license"></a>
  <img src="https://img.shields.io/badge/desktop-macOS%20%7C%20Windows%20%7C%20Linux-15191a" alt="macOS, Windows, and Linux desktop app">
  <img src="https://img.shields.io/badge/built_with-Rust-b8aaa0" alt="Built with Rust">
</p>

<p align="center"><strong>One skill library. Every project gets only what it needs.</strong></p>

Kitter is a desktop app and CLI for managing Agent Skills across projects. Keep your skills in one library, install the right combination for each project, and update them in one place.

Built entirely in Rust with GPUI, Kitter pairs a straightforward interface with a small footprint and smooth native performance.

<p align="center">
  <img src="./assets/readme/skill-workflow.png" width="100%" alt="Kitter maintains one skill library and links selected skills to projects and user-level installations">
</p>

## Why Kitter

Working across projects often means maintaining several copies of the same skill and keeping track of what each agent can use. Kitter keeps those connections visible:

- **Maintain once** — projects link to the same skill source, so one update reaches every linked installation.
- **Choose per project** — give each project its own skill set, with user-level installation for skills you use everywhere.
- **See what is active** — inspect the skills each agent discovers, including installations outside Kitter, along with their sources and estimated context cost.

## Install Kitter

Download the app for your platform from [GitHub Releases](https://github.com/what1f/kitter/releases/latest).

- **macOS (Apple Silicon / Intel)** — choose the `macos-arm64.dmg` (Apple Silicon) or `macos-x86_64.dmg` (Intel) download, open the `.dmg` and drag `Kitter.app` into `Applications`.
- **Windows (x64)** — download `Kitter-<version>-desktop-windows-x86_64.exe` and run it directly.
- **Linux (x64)** — extract `Kitter-<version>-desktop-linux-x86_64.tar.gz` and run `./Kitter` from the extracted `Kitter` directory.

Kitter is not yet signed with an Apple Developer ID. If macOS blocks the first launch, confirm that you downloaded it from the official release, then go to **System Settings → Privacy & Security → Open Anyway** and follow the prompts. See [Apple’s instructions](https://support.apple.com/102445).

You can also run the following command, then open Kitter again:

```bash
xattr -dr com.apple.quarantine /Applications/Kitter.app
```

The desktop app and CLI are separate release artifacts built on the same core. Standalone CLI packages for macOS, Windows, and Linux are available from [GitHub Releases](https://github.com/what1f/kitter/releases/latest). The built-in Kitter skill resolves that standalone CLI and guides you through downloading it when needed.

## Manage your skills with Kitter

### 1. Build one library

Use **+** to add skills from a local folder, GitHub or a skills.sh-compatible source, or a Claude plugin source. If skills are already scattered across projects, choose **Existing installations** to inspect and adopt them without moving their source directories.

Kitter keeps one maintained source for each skill. Open its **Installs** tab to immediately see every project using it, every installation location, and the agents that can discover it.

<p align="center">
  <img src="./assets/readme/skill-library.en.png" width="100%" alt="Kitter skill library showing one managed skill installed across several projects">
</p>

### 2. Install only where needed

Select a skill, choose a project, then install it into the shared `.agents/skills` directory or an agent-specific directory. Kitter creates managed links instead of independent copies, so projects can use different combinations without creating update drift.

<p align="center">
  <img src="./assets/readme/install-skill.en.png" width="100%" alt="Kitter installation dialog for selecting a project and agent targets">
</p>

Skills you use across all projects can also be installed at the user level.

### 3. Verify what is actually active

Open **Projects** to see the complete effective skill set for every agent—not just installations managed by Kitter. The view discovers project, parent, user-level, built-in, and plugin-provided capabilities, then shows where each one came from.

The per-agent token estimate helps you spot skills that add unnecessary context overhead.

<p align="center">
  <img src="./assets/readme/project-effective-skills.en.png" width="100%" alt="Kitter project view showing managed and unmanaged effective skills, plugins, agents, and estimated context cost">
</p>

### 4. Update once

Run **Check for updates** from the desktop app or use `kitter check` and `kitte