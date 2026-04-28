# <img src="site/assets/logo.png" alt="" width="28">&nbsp;revdiff &nbsp;<a href="https://github.com/umputun/revdiff/actions/workflows/ci.yml"><img src="https://github.com/umputun/revdiff/actions/workflows/ci.yml/badge.svg" alt="build"></a> <a href="https://coveralls.io/github/umputun/revdiff?branch=master"><img src="https://coveralls.io/repos/github/umputun/revdiff/badge.svg?branch=master" alt="Coverage Status"></a> <a href="https://goreportcard.com/report/github.com/umputun/revdiff"><img src="https://goreportcard.com/badge/github.com/umputun/revdiff" alt="Go Report Card"></a>

TUI for reviewing diffs, files, and documents with inline annotations. Outputs structured annotations to stdout on quit, making it easy to pipe results into AI agents, scripts, or other tools.

Built for a specific use case: reviewing code changes, plans, and documents without leaving a terminal-based AI coding session (e.g., Claude Code). Just enough UI to navigate diffs and files, annotate specific lines, and return the results to the calling process - no more, no less.

## Features

- Structured annotation output to stdout - pipe into AI agents, scripts, or other tools
- Full-file diff view with syntax highlighting
- Intra-line word-diff: highlights the specific changed words within paired add/remove lines using a brighter background overlay, off by default — enable with `--word-diff` or toggle with `W`
- Collapsed diff mode: shows final text with change markers, toggle with `v`
- Word wrap mode: wraps long lines at viewport boundary with `↪` continuation markers, toggle with `w`
- Horizontal scroll overflow indicators: truncated diff lines show `«` / `»` markers at the edges to signal hidden content off-screen
- Vertical scrollbar thumb: a thicker `┃` segment on pane right borders indicates the visible portion of long diffs, file trees, and markdown TOCs; thumb size and position track scroll progress automatically
- Line numbers: side-by-side old/new line number gutter for diffs, single column for full-context files, toggle with `L`
- Mercurial support: auto-detects hg repos, translates git-style refs (HEAD, HEAD~N) to Mercurial revsets
- Jujutsu support: auto-detects jj repos (including colocated git+jj), translates git-style refs to jj revsets (`HEAD` → `@-`, `HEAD~N` → `@` plus N+1 dashes); `--all-files` supported
- Blame gutter: shows author name and commit age per line, toggle with `B`
- Annotate any line in the diff (added, removed, or context) plus file-level notes
- Single-file auto-detection: when a diff contains exactly one file, hides the tree pane and gives full terminal width to the diff view
- Two-pane TUI: file tree (left) + colorized diff viewport (right)
- Vim-style `/` search within diff with `n`/`N` match navigation
- Hunk navigation to jump between change groups
- Annotation list popup (`@`): browse all annotations across files, jump to any annotation
- Filter file tree to show only annotated files
- Status line with filename, diff stats, hunk position, line number, and mode indicators
- Help overlay (`?`) showing all keybindings organized by section
- Info popup (`i`) showing launch scope (mode, VCS, ref, filters, file/status counts, aggregate `+/-` line stats), the optional `--description` prose, and the commit log subject + body for every commit in the current ref range (git/hg/jj) — useful for restoring narrative context when reviewing PR-style diffs
- Markdown TOC navigation: single-file markdown files in context-only mode show a table-of-contents pane with header navigation and active section tracking
- All-files mode: browse and annotate all tracked files with `--all-files` (git `ls-files` or jj `file list`), filter with `--include` and `--exclude`
- No-VCS file review: `--only` files outside a VCS repo (or not in any diff) are shown as context-only with full annotation support
- Scratch-buffer review: annotate arbitrary piped or redirected text with `--stdin`, optionally naming it with `--stdin-name`
- Pi package: launch revdiff from pi, capture annotations, and keep them visible in a widget and right-side panel until you apply or clear them
- Review history: auto-saves annotations and diffs to `~/.config/revdiff/history/` on quit as a safety net
- Fully customizable colors via environment variables, CLI flags, or config file
- Custom keybindings: remap any key via config file, export defaults with `--dump-keys`

![revdiff screenshot](site/assets/screenshot.png)

## Requirements

- `git`, `hg`, or `jj` (used to generate diffs; optional when using `--only` or `--stdin`)

## Installation

**Homebrew (macOS/Linux):**

```bash
brew install umputun/apps/revdiff
```

**Arch Linux (AUR):**

```bash
paru -S revdiff
```

**Debian/Ubuntu (.deb):**

```bash
# download the latest .deb for your architecture from GitHub Releases
sudo dpkg -i revdiff_*.deb
```

**RPM-based (Fedora, RHEL, etc.):**

```bash
# download the latest .rpm for your architecture from GitHub Releases
sudo rpm -i revdiff_*.rpm
```

**Binary rel