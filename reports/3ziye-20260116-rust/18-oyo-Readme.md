<div align="center">

# oyo

A diff viewer that works **two ways**:
**step through changes** or **review a classic scrollable diff**.


<!-- Demo source: https://github.com/user-attachments/assets/0f43b54b-69fe-4cf3-9221-a7749872342b -->
https://github.com/user-attachments/assets/0f43b54b-69fe-4cf3-9221-a7749872342b

</div>

**oyo** extends traditional diffs with an optional step-through mode. Use it like a normal diff viewer with scrolling and hunk navigation, or step through changes one at a time and watch the code evolve. You can switch between both modes at any time.

## Two ways to use oyo

### 1. Classic diff (scroll-only)
Review all changes at once, scroll freely, and jump between hunks, just like a traditional diff viewer.

- Scroll the full diff
- Jump between hunks
- No stepping required

Enable with:
- `oy --no-step`
- Toggle in-TUI with `s`
- Set `stepping = false` in config

### 2. Step-through review (default)
Apply changes incrementally and watch the file transform from old → new.

- Step change-by-change
- See precise evolution of the code
- Useful for large refactors or careful reviews

oyo does **not** replace classic diffs, it adds a new way to review them.


## Features

- **Classic diff mode (no-step)**
  Scroll the full diff with hunk navigation, no stepping required
- **Step-through navigation**
  Move through changes one at a time with keyboard shortcuts
- **Hunk navigation**
  Jump between groups of related changes in both modes
- **Four view modes**:
  - **Unified**: Watch the code morph from old to new state
  - **Split**: See old and new versions with synchronized stepping
  - **Evolution**: Watch the file evolve, deletions simply disappear
  - **Blame**: Per-line git blame gutter (opt-in)
- **Word-level diffing**: See exactly which words changed within a line
- **Multi-file support**: Navigate between changed files with preserved positions
- **Search**: Regex search with to jump between matches
- **Syntax highlighting**: Toggle on/off for code-aware coloring (auto-enabled in no-step mode)
- **Blame hints**: One-shot or toggle blame previews while stepping (opt-in)
- **Command palette**: Search for commands and files without leaving the diff
- **Line wrap**: Toggle wrapping for long lines
- **Fold unchanged blocks**: Toggle to collapse long context sections
- **Animated transitions**: Smooth fade in/out animations as changes are applied
- **Playback**: Automatically step through all changes at a configurable speed
- **Git integration**: Works as a git external diff tool or standalone
- **Commit picker**: Browse recent commits and pick ranges interactively (`oy view`)
- **Themes**: Built-in themes plus `.tmTheme` syntax themes (configurable, with light/dark variants)
- **Configurable**: XDG config file support for customization

## Installation

### Homebrew (macOS)

```bash
brew install ahkohd/oyo/oy
```

### AUR (Arch Linux)

```bash
paru -S oyo
```

### Cargo

```bash
cargo install oyo
```

## Usage

### Classic diff (scroll-only)

```bash
oy --no-step
# or toggle in-app with `s`
```

### Step-through diff

```bash
oy
```

### Compare files

```bash
oy old.rs new.rs
```

### Commit picker

```bash
oy view
```

### View modes

```bash
oy old.rs new.rs --view split
oy old.rs new.rs --view evolution
```

### Autoplay

```bash
oy old.rs new.rs --autoplay
oy old.rs new.rs --speed 100
```

### Git ranges

```bash
oy --range HEAD~1..HEAD
oy --range main...feature
```

### Staged changes

```bash
oy --staged
```

---

## Git Integration

### Recommended (`git difftool`)

```bash
git difftool -y --tool=oy
```

`~/.gitconfig`:

```gitconfig
[difftool "oy"]
    cmd = oy "$LOCAL" "$REMOTE"

[difftool]
    prompt = false

[alias]
    d = difftool -y --tool=oy
```

> Note: keep your pager (`less`, `moar`, `moor`) for `git diff`.
> Do **not** set `core.pager` or `interactive.diffFilter` to `oy`.

---

## Jujutsu (jj)

```toml
[ui]
paginate = "never"
diff-formatter = ["oy", "$left", "$right"]

[diff-tools.oy]
command = ["oy", "$left", "$right"]
```

### Keyboard Shortcuts

**Vim-style counts**: Most navigation commands support count prefixes (e.g., `10j` moves 10 steps forward, `5J` scrolls down 5 lines).

| Key | Action |
|-----|--------|
| `↓` / `j` | Next step (scrolls in no-step mode; moves file selection when focused) |
| `↑` / `k` | Previous step (scrolls in no-step mode; moves file selection when focused) |
| `→` / `l` | Next hunk (scrolls in no-step mode) |
| `←` / `h` | Previous hunk (scrolls in no-step mode) |
| `b` | Jump to beginning of current hunk (scrolls in no-step mode) |
| `e` | Jump to end of current hunk (scrolls in no-step mode) |
| `gb` | Blame current step (opt-in, step mode) |
| `p` / `P` | Peek change (modified → old → mixed) / Peek old hunk |
| `y` / `Y` | Yank line/hunk to clipboard |
| `/` | Search (diff pane, regex) |
| `n` / `N` | Next/previous match |
| `:line` / `:h<num>` / `:s<num>` | Go to line / hunk / step |
| `<` | First applied step |
| `>` | Last step |
|