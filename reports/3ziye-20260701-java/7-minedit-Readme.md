# Minedit

Minedit is an experimental NeoForge mod for building and editing Minecraft structures with AI models through OpenRouter or a local bridge for Codex or Cursor.

Select a footprint with a stick, describe what you want, and Minedit asks a model to generate compact builder code that places blocks in the selected area. It can also edit existing builds with compact line-aware patches, generate builds in focused stages, and run local bridge agent modes.

## Status and Risk

Minedit is a work in progress. Expect things to break.

This mod sends prompts to the provider you configure. OpenRouter requests use the API key you configure. Codex local bridge requests use your local Codex/OpenAI login and may consume Codex, ChatGPT, or OpenAI plan limits. Cursor local bridge requests use your local Cursor login or API key and may consume Cursor plan limits. Depending on your provider, model, account, and usage, requests may cost money or consume plan limits. You are responsible for all usage and charges caused by your configured provider. Use this mod at your own risk. The author is not responsible for unexpected costs, world changes, broken builds, broken saves, or other side effects.

Your OpenRouter API key is stored in plaintext in your Minecraft game directory at `config/minedit.properties`. It is not stored per-world. Do not share this file, screenshots of it, modpacks containing it, or support logs that include it.

Back up worlds before testing large builds, staged builds, agent builds, or edits.

## Requirements

- Minecraft `26.1.2`
- NeoForge `26.1.2.73`
- Java 25 for development/building
- OpenRouter API key for OpenRouter mode
- Node.js 18+ and the Codex CLI for local Codex bridge mode
- Cursor CLI for local Cursor bridge mode

## Installation

You can either download a prebuilt jar from the GitHub Releases page or build it yourself.

### Download a Release

1. Download the latest jar from the [Minedit releases page](https://github.com/Angais/minedit/releases).
2. Copy the jar into your Minecraft `mods` folder.
3. Start the NeoForge profile.

### Build from Source

```sh
./gradlew build
```

Copy the jar from `build/libs/` into your Minecraft `mods` folder, then start the NeoForge profile.

## Quick Start

Minedit uses OpenRouter by default.

```mcfunction
/apikey <your-openrouter-key>
/model openai/gpt-5.5
```

Select two X/Z footprint corners by right-clicking blocks with a stick, then run:

```mcfunction
/build a detailed medieval blacksmith
```

Minedit uses the selected X/Z area as the footprint. Height is not capped by the selection.

When the second corner is selected, Minedit prints a short coordinate summary and a reusable `/selection set ...` command in chat. Save that command if you want to restore the same area later.

## Build Modes

### Normal Build

One model call generates the whole build:

```mcfunction
/build a cute house
```

Build mode clears existing non-air blocks in the selected footprint before placing the generated structure.

### Staged Build

Several focused model calls build the structure in phases:

```mcfunction
/build stages a detailed wizard tower
```

The staged builder currently runs these stages:

1. Foundation and frame
2. Walls, openings, doors, and windows
3. Roof, ceilings, stairs, and vertical access
4. Interior lighting and furniture
5. Exterior detail and landscaping
6. Final corrections and polish

Each stage receives the previous stage code as context and should only output incremental work for the current stage. This usually costs more than `/build`, but it gives the model more focus per phase.

### Local Agent Build

Agent modes work with the local bridge through Codex or Cursor:

```mcfunction
/provider codex-local
# or
/provider cursor
/build agent <prompt>
/build agent step-by-step <prompt>
```

`/build agent <prompt>` asks the local agent provider to draft, preview, and revise before Minecraft places the final build.

`/build agent step-by-step <prompt>` places the build in multiple visible steps. Codex uses Minedit dynamic tools such as `place_step`, `render_preview`, `inspect_status`, and `finish_build`. Cursor uses the bridge's phased step generator and emits placement batches as each phase completes.

## Editing

Use `/edit` to modify the selected area based on its current blocks:

```mcfunction
/edit make the roof steeper and add windows
```

Use quick edit for small targeted patches:

```mcfunction
/edit quick remove the flower and change the oak planks to spruce
```

Normal edit and quick edit use a compact line-aware representation of the current build, so models can emit small patches like `api.replaceLine(...)`, `api.clearLine(...)`, `api.set(...)`, or `api.fill(...)` instead of rebuilding unchanged geometry.

Set quick edit reasoning effort:

```mcfunction
/edit set quickeffort low
```

## Local Bridge

The local bridge lets Minecraft talk to `codex app-server` or Cursor CLI through a localhost HTTP server.

Requirements:

- Node.js 18+
- 