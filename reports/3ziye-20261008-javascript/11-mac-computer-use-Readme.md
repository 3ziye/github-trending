<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/mac-computer-use-logo-dark.svg">
  <img src="assets/mac-computer-use-logo-light.svg" alt="mac-computer-use" width="720">
</picture>

### Give your agent hands on your Mac.

Observe windows. Take action. Verify the result.

**English** · [简体中文](README.zh-CN.md)

![An illustrative Observe, Act, Verify workflow for mac-computer-use](assets/readme-hero.gif)

<sub>Illustrative workflow. <a href="assets/readme-hero-poster.png">Static preview</a></sub>

[Get started](#get-started) · [Capabilities](#capabilities) · [How it works](#observe--act--verify) · [Compatibility](#one-skill-many-agents) · [Download](https://github.com/To3akaRin/mac-computer-use/releases/latest)

[![CI](https://github.com/To3akaRin/mac-computer-use/actions/workflows/ci.yml/badge.svg)](https://github.com/To3akaRin/mac-computer-use/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/To3akaRin/mac-computer-use)](https://github.com/To3akaRin/mac-computer-use/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![macOS](https://img.shields.io/badge/macOS-14%2B-black?logo=apple)](#requirements)

</div>

Turn a desktop task into an agent workflow. **mac-computer-use** connects native Mac windows, Accessibility controls, and embedded Chromium pages to an agent that can observe a target, operate it, and check what actually happened. Built on the open [Agent Skills standard](https://agentskills.io/), it works with runtimes that can read the full skill package and execute commands on your Mac.

## From reference photos to a rotatable 3D exhibition space. 12 minutes, without touching the mouse.

![A real browser recording of the user-provided central exhibition space model rotating](assets/showcase-3d.gif)

**Real-world example: modeling a central exhibition space in 3D.** A central column, overhead ring, curved cabinets, portal frames, terminals, and a checkout counter form a three-dimensional space you can rotate and inspect in a browser.

**3,388 triangles · 117 meshes · a single GLB file of approximately 218 KiB.** The animation was recorded directly from the model viewer, showing the actual geometry from multiple angles. The model includes an editable Blender source file; dimensions were estimated from reference photos.

[View the full-size still](assets/showcase-3d-poster.jpg) · [Asset provenance and recording notes (Chinese)](docs/media.md)

## Get started

Install the complete skill with [Skills CLI](https://github.com/vercel-labs/skills), then select your agent:

```bash
npx skills add To3akaRin/mac-computer-use
```

Your agent needs to execute locally on a **Mac with macOS 14+ and Swift 6 Command Line Tools**. CDP commands also require **Node.js 22.4+**. See [requirements](#requirements) for permissions and setup.

Prefer a manual install? Download the skill ZIP and SHA-256 from [Releases](https://github.com/To3akaRin/mac-computer-use/releases/latest), or clone this repository and choose a confirmed skill directory:

```bash
sh scripts/install.sh --skills-dir "/path/to/your/skills" --dry-run
sh scripts/install.sh --skills-dir "/path/to/your/skills"
```

The installer copies the full `mac-computer-use/` directory and refuses to overwrite an existing installation. Keep the accompanying source files and scripts; copying only `SKILL.md` is not enough. See the [runtime installation guide (Chinese)](references/runtimes.md).

### Start with a task

```text
“Turn this reference image into a 3D model I can inspect.”

“Use this app to connect to my server and complete the deployment.
Check the result at every step.”

“Find the target window, enter this Chinese text in the specified field,
and read it back to verify it.”

“Click this button, check whether the app's state actually changed,
and capture a screenshot of the result.”
```

These are task examples for your agent to plan. What it can complete depends on the target app's controls, interfaces, permissions, and the tools available to the agent. The skill supplies desktop execution tools; your agent supplies the reasoning and orchestration.

## Capabilities

| Capability | What your agent can do |
| --- | --- |
| **See the target** | List windows, processes, titles, and geometry. Read Accessibility (AX) controls and CDP page structure. |
| **Find a control path** | Inspect application bundles, scripting dictionaries, URL schemes, and candidate debugging ports. |
| **Enter text precisely** | Set and read back AX values, send native Unicode input, and use CDP `Input.insertText` for fields and rich text. |
| **Interact with apps** | Click, hover, scroll, and send shortcuts through native input or Chromium renderer events. |
| **Use the foreground carefully** | Prefer background channels; check user inactivity, target state, and a session lock before foreground actions. Restore focus when safe. |
| **Keep coordinates grounded** | Distinguish logical p