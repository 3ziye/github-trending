![Herdr Annotate](assets/herdr-annotate.webp)

# herdr-annotate
Annotate inside [Herdr](https://github.com/herdrdev/herdr): comment on any terminal text, review whole Markdown documents and your agent's replies, and send the feedback straight back to the agent. Document review is powered by [plannotator-tui](https://github.com/plannotator/plannotator-tui), which also runs on its own outside Herdr.

<p align="center">
  <a href="https://github.com/backnotprop/plannotator">
    <img src="./assets/star-plannotator.svg" width="280" alt="Like this? Star Plannotator">
  </a>
</p>

**Watch the demos**

[![Demo: Full install](https://img.shields.io/badge/%E2%96%B6%20Demo%3A%20Full%20install-f7ca5e?style=flat-square&labelColor=171429)](https://x.com/plannotator/status/2093419561077154287)
[![Demo: Lite install](https://img.shields.io/badge/%E2%96%B6%20Demo%3A%20Lite%20install-c9c6f1?style=flat-square&labelColor=171429)](https://x.com/plannotator/status/2092757422322627008)

## Requirements

- Herdr 0.8.0 or later
- [Bun](https://bun.sh/)
- macOS, Linux, or Windows

On Linux, install `wl-clipboard`, `xclip`, or `xsel` for clipboard access.

On Windows, native Herdr plugin support is preview/best-effort. Bun must be on `PATH`. Clipboard access uses PowerShell; no extra clipboard package is required. The install, keybinding, configuration check, reload, and use instructions below also apply on Windows.

## Install

Pick one. Installing the other later just swaps it (same plugin id).

<img src="assets/install-full.svg" width="200" align="left" alt="Full">

**Full:** annotate terminal text, review documents and agent replies, send feedback to the agent.
Wraps [Plannotator TUI](https://github.com/plannotator/plannotator-tui) (macOS and Linux today). [Demo](https://x.com/plannotator/status/2093419561077154287)

```sh
herdr plugin install plannotator/herdr-annotate
```

<br clear="all">

<img src="assets/install-lite.svg" width="200" align="left" alt="Lite">

**Lite:** the simple version: select text, `prefix+a`, comment in a popover. [Demo](https://x.com/plannotator/status/2092757422322627008)

```sh
herdr plugin install plannotator/herdr-annotate/lite
```

<br clear="all">

> **Required.** Bind the keys in Herdr's config.

<details open>
<summary><b>Full install keys:</b> terminal annotations + document and agent-reply review</summary>

```toml
# Terminal annotations
[[keys.command]]
key = "prefix+a"
type = "plugin_action"
command = "annotate.capture"
description = "annotate text"

[[keys.command]]
key = "prefix+shift+a"
type = "plugin_action"
command = "annotate.copy-context"
description = "copy annotations as context"

[[keys.command]]
key = "prefix+m"
type = "plugin_action"
command = "annotate.manage"
description = "manage annotations"

# Document review (plannotator-tui)
[[keys.command]]
key = "prefix+o"
type = "plugin_action"
command = "annotate.open"
description = "review documents in this folder"

[[keys.command]]
key = "prefix+shift+o"
type = "plugin_action"
command = "annotate.last"
description = "review the agent's last reply"
```

</details>

<details>
<summary><b>Lite install keys:</b> terminal annotations only</summary>

```toml
[[keys.command]]
key = "prefix+a"
type = "plugin_action"
command = "annotate.capture"
description = "annotate text"

[[keys.command]]
key = "prefix+shift+a"
type = "plugin_action"
command = "annotate.copy-context"
description = "copy annotations as context"

[[keys.command]]
key = "prefix+m"
type = "plugin_action"
command = "annotate.manage"
description = "manage annotations"
```

</details>

Check and reload:

```sh
herdr config check
herdr server reload-config
```

## Use

### Annotate terminal text

| Key | Action |
|---|---|
| `Ctrl+B A` | comment on the selected text · `Ctrl+S` saves |
| `Ctrl+B Shift+A` | copy all annotations as Markdown |
| `Ctrl+B M` | manage · `y` copy one · `c` copy all · `Shift+C` copy and archive · `Tab` archives (`y` copy · `u` restore · `d d` delete) |

### Review documents and agent replies

Full install. Works with Claude Code, Codex, pi, Copilot CLI, Droid, Oh My Pi, Hermes CLI and OpenCode (1 and 2).

| Key | Opens |
|---|---|
| `Ctrl+B O` | this folder, with a file tree |
| `Ctrl+B Shift+O` | the agent's recent replies |
| Ctrl-click a `file://…md` link | that file |

**Send** (or `E`) makes the review the agent's next message. `q` closes.

| Option | Where |
|---|---|
| Agents request reviews themselves | `npx skills add plannotator/herdr-annotate --skill plannotator-tui -g` |
| Open as full tab, split, or popup | `[herdr] placement = "overlay" \| "split" \| "popup"` in `~/.config/plannotator-tui/config.toml` |
| Use without Herdr | [plannotator-tui](https://github.com/plannotator/plannotator-tui) |

### Remote sessions

Over SSH or `herdr --remote`, the plugin runs on the **server**, and two things get in the way:
Herdr's default copy-on-select clears the selection on mouse-up, and the prefix keypress
clears whatever selection remains before a bou