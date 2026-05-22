<img alt="Usagi Logo: pixel art bunny, Usagi Engine - Rapid 2D Prototyping" src="/website/card-logo.png" />

# Usagi - Simple 2D Game Engine for Rapid Prototyping

Usagi is a 2D game engine for making pixel art games in **Lua** 5.5. It features
live reload, single-command cross-platform export, and a pause menu with input
remapping built in.

Usagi is free software made by [Brett Chalupa](https://brettmakesgames.com) and
dedicated to the public domain.
[Support development of the engine by buying me a coffee.](https://www.buymeacoffee.com/brettchalupa)

<video controls crossorigin="anonymous" type="video/mp4" src="https://assets.brettchalupa.com/usagi.mp4"></video>

**Links:** [usagiengine.com](https://usagiengine.com),
[Discord](https://usagiengine.com/discord),
[r/UsagiEngine](https://reddit.com/r/UsagiEngine),
[Quickstart video](https://www.youtube.com/watch?v=0i1wIm6c6Rw),
[YouTube Playlist](https://www.youtube.com/playlist?list=PL0qDutCc8IQhkbS53etm9xV06XgEb4BEN)

## Install

**Linux, macOS:**

```sh
curl -fsSL https://usagiengine.com/install.sh | sh
```

**Windows (PowerShell):**

```powershell
irm https://usagiengine.com/install.ps1 | iex
```

The installer fetches the latest release from GitHub, verifies its SHA-256
checksum, installs `usagi` to `~/.usagi/bin/` (or `%USERPROFILE%\.usagi\bin\` on
Windows), and adds it to `PATH`.

Manual download:
[GitHub Releases](https://github.com/brettchalupa/usagi/releases/latest) or
[itch.io](https://brettchalupa.itch.io/usagi)

Latest release: **v1.0.0**.

[View the changelog.](https://usagiengine.com/changelog)

![Rotating cube demo](/website/demo.gif)

## Features

- **Live reload.** `usagi dev` watches your code and assets; saves apply without
  losing game state. Tweak a sprite in your editor and see it update instantly.
- **One-command export.** `usagi export` packages your game for Linux, macOS,
  Windows, and the web.
- **Pause menu, free.** Built-in pause menu with sfx and music volume,
  fullscreen toggle, and per-game keyboard + gamepad remapping.
- **Easy save data.** One function to save and load your game state as a Lua
  table.
- **Small, fixed API.** You can't do everything, but you've got what you need to
  make a great 2D game.
- **Constraints to inspire creativity.** 320x180 default resolution, 16x16
  default sprite grid, a single `sprites.png` for textures.

Bring your own sound effects, sprite editor, and music tools.

![Menu preview showing Continue, Settings, Clear Save Data, Reset Game, and Quit options](/website/menu.png)

## Hello, Usagi

Bootstrap a project and start it in dev mode:

```sh
usagi init my_game
cd my_game
usagi dev
```

`init` writes `main.lua` (with `_init` / `_update` / `_draw` stubs),
`.luarc.json` for Lua LSP support, `.gitignore`, `meta/usagi.lua` (API type
stubs), and `USAGI.md` (a copy of these docs).

Edit `main.lua`, save, and the running game picks up the change without
restarting or losing state. Drawing "Hello, Usagi!" looks like:

```lua
function _draw(_dt)
  gfx.clear(gfx.COLOR_BLACK)
  gfx.text("Hello, Usagi!", 10, 10, gfx.COLOR_WHITE)
end
```

## Updating Usagi

Replace the `usagi` binary with a newer release, or run `usagi update` to fetch
the latest. Then run `usagi refresh` inside a project to refresh the LSP type
stubs and embedded docs (`meta/usagi.lua`, `.luarc.json`, `USAGI.md`). It won't
touch `main.lua`.

## Feedback and Issues

Open a [GitHub issue](https://github.com/brettchalupa/usagi/issues/new/choose)
for feedback, requests, and bugs. Search first to avoid duplicates.

## Goals and non-goals

Usagi is for rapid 2D pixel-art prototyping in Lua. It's a great fit if you want
to quickly try out an idea, if you're new to game programming, if you've hit
Pico-8's token limit, or if you want something simpler than Love2D.

It is **not** a fantasy console or a Love2D replacement. It doesn't target
mobile or VR, and it isn't built for medium-to-large polished games.

**Why Lua:** small, widely used in game tooling, and powerful enough to stay out
of your way.

## Project Layout

An Usagi game is either a single `.lua` file or a directory with a `main.lua` in
it. Additional `.lua` files anywhere under the project root can be loaded with
stock Lua's `require`. Optional assets live alongside the source code. Here's
what a folder structure could look like for a multi-file project:

```
my_game/
  main.lua           -- required: your game's entry point
  sprites.png        -- optional: 16×16 sprite sheet (PNG with alpha)
  palette.png        -- optional: custom palette (1px tall, one color per pixel)
  font.png           -- optional: custom font (bake with `usagi font bake`)
  enemies.lua        -- optional: require "enemies"
  data/
    level.json       -- optional: JSON data, loadable with `usagi.read_json("level.json")
    dialog.txt       -- optional: text data, loadable with `usagi.read_text("dialog.txt")
  scenes/
    main_menu.lua    -- optional: require "scenes.main_menu" - source code can be in fo