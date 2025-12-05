# treemd

[![Crates.io](https://img.shields.io/crates/v/treemd.svg)](https://crates.io/crates/treemd)
[![Documentation](https://docs.rs/treemd/badge.svg)](https://docs.rs/treemd)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/github/actions/workflow/status/epistates/treemd/rust.yml?branch=main)](https://github.com/epistates/treemd/actions)

A markdown navigator with tree-based structural navigation. Like `tree`, but interactive—navigate markdown documents using an expandable/collapsible heading tree with a synchronized content view.

<img src="assets/screenshot.webp" alt="treemd" style="width: 100%; max-width: 100%; margin: 20px 0;"/>

## Overview

**treemd** is a modern markdown viewer that combines the structural clarity of the `tree` command with powerful interactive navigation. Whether you're exploring large documentation files, analyzing markdown structure, or just reading comfortably in your terminal, treemd provides both CLI tools for scripting and a beautiful TUI for interactive exploration.

## Features

### Interactive TUI

- **Dual-pane interface** - Navigate outline while viewing content
- **Interactive mode** - Navigate, edit, and interact with all markdown elements (tables, checkboxes, links, code blocks)
- **Table navigation & editing** - Navigate cells with vim keys (`hjkl`), edit cell content in-place, copy cells/rows/tables
- **Checkbox toggling** - Toggle task list items with instant file updates
- **Live editing** - Edit files in default editor with auto-reload (respects `$VISUAL`/`$EDITOR`)
- **Link following** - Follow markdown links with visual popup, supports anchor/file/wikilink/external URLs
- **Navigation history** - Back/forward between files with full state preservation
- **Syntax highlighting** - 50+ languages with full syntect integration
- **Vim-style navigation** - `j`/`k`, `g`/`G`, `d`/`u`, `p` (parent) for efficient browsing
- **Search & filter** - Press `/` to filter headings in real-time
- **Collapsible tree** - Expand/collapse sections with `Space`/`Enter`
- **Bookmarks** - Mark positions (`m`) and jump back (`'`)
- **Adjustable layout** - Toggle outline visibility, resize panes
- **Rich rendering** - Bold, italic, inline code, lists, blockquotes, code blocks, tables with box-drawing characters

### CLI Mode

- **Query language** - jq-like syntax for extracting markdown elements (`-q '.h2 | text'`)
- **List headings** - Quick overview of document structure
- **Tree visualization** - Hierarchical display with box-drawing
- **Section extraction** - Extract specific sections by heading name
- **Smart filtering** - Filter by text or heading level
- **Multiple formats** - Plain text, JSON output
- **Statistics** - Count headings by level
- **Stdin support** - Pipe markdown content (`cat doc.md | treemd -q '.h'`)

**treemd** is incredibly powerful as a CLI utility. Using the `--tree` visualizations with `--section` enables rapid piecewise consumption of even the largest `.md` files. The query language brings jq-like power to markdown extraction.

## Installation

### From crates.io

```bash
cargo install treemd
```

### From source

```bash
git clone https://github.com/epistates/treemd
cd treemd
cargo install --path .
```

### Using a package manager

`treemd` is available as a native package on Arch Linux and NetBSD.

**Arch Linux ([`extra`](https://archlinux.org/packages/extra/x86_64/treemd/) repo):**

```bash
pacman -S treemd
```

**NetBSD:**

```bash
pkgin install treemd
```

[Homebrew](https://brew.sh) hosts precompiled binaries for macOS and Linux.
To install it, simply run:

```bash
brew install treemd
```

## Usage

### TUI Mode (Interactive - Default)

Simply run treemd without flags to launch the interactive interface:

```bash
treemd README.md
```

**Keyboard Shortcuts:**

*Navigation:*
- `j/k` or `↓/↑` - Navigate up/down
- `g/G` - Jump to top/bottom
- `p` - Jump to parent heading
- `d/u` - Page down/up (in content)
- `Tab` - Switch between outline and content
- `1-9` - Jump to heading 1-9 (instant access)

*Tree Operations:*
- `Enter/Space` - Toggle expand/collapse
- `h/l` or `←/→` - Collapse/expand heading

*UX Features:*
- `w` - Toggle outline visibility (full-width content)
- `[` `]` - Decrease/increase outline width (20%, 30%, 40%)
- `m` - Set bookmark at current position
- `'` - Jump to bookmarked position

*Link Following:*
- `f` - Enter link follow mode (shows popup with all links)
- `Tab`/`Shift+Tab` - Navigate through links
- `j/k` or `↓/↑` - Navigate links (in link mode)
- `1-9` - Jump directly to link by number
- `p` - Jump to parent heading's links (stays in link mode)
- `Enter` - Follow selected link (opens browser, loads file, or jumps to anchor)
- `b`/`Backspace` - Go back to previous file
- `Shift+F` - Go forward in navigation history
- `Esc` - Exit link follow mode

*Interactive Mode:*
- `i` - Enter interactive mode (navigate all interactive elemen