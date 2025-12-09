# codemap 🗺️

> **codemap — a project brain for your AI.**
> Give LLMs instant architectural context without burning tokens.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Go](https://img.shields.io/badge/go-1.21+-00ADD8.svg)

![codemap screenshot](assets/codemap.png)

## Table of Contents

- [Why codemap exists](#why-codemap-exists)
- [Features](#features)
- [How It Works](#%EF%B8%8F-how-it-works)
- [Performance](#-performance)
- [Installation](#installation)
- [Usage](#usage)
- [Diff Mode](#diff-mode)
- [Dependency Flow Mode](#dependency-flow-mode)
- [Skyline Mode](#skyline-mode)
- [Supported Languages](#supported-languages)
- [Claude Integrations](#claude-integrations)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

## Why codemap exists

Modern LLMs are powerful, but blind. They can write code — but only after you ask them to burn tokens searching or manually explain your entire project structure.

That means:
*   🔥 **Burning thousands of tokens**
*   🔁 **Repeating context**
*   📋 **Pasting directory trees**
*   ❓ **Answering “where is X defined?”**

**codemap fixes that.**

One command → a compact, structured “brain map” of your codebase that LLMs can instantly understand.

## Features

- 🧠 **Brain Map Output**: Visualizes your codebase structure in a single, pasteable block.
- 📉 **Token Efficient**: Clusters files and simplifies names to save vertical space.
- ⭐️ **Smart Highlighting**: Automatically flags the top 5 largest source code files.
- 📂 **Smart Flattening**: Merges empty intermediate directories (e.g., `src/main/java`).
- 🎨 **Rich Context**: Color-coded by language for easy scanning.
- 🚫 **Noise Reduction**: Automatically ignores `.git`, `node_modules`, and assets (images, binaries).

## ⚙️ How It Works

**codemap** is a fast Go binary with minimal dependencies:
1.  **Scanner**: Instantly traverses your directory, respecting `.gitignore` and ignoring junk.
2.  **Analyzer**: Uses [ast-grep](https://ast-grep.github.io/) to parse imports/functions across 18 languages.
3.  **Renderer**: Outputs a clean, dense "brain map" that is both human-readable and LLM-optimized.

## ⚡ Performance

**codemap** runs instantly even on large repos (hundreds or thousands of files). This makes it ideal for LLM workflows — no lag, no multi-tool dance.

## Installation

### Homebrew (macOS/Linux)

```bash
brew tap JordanCoin/tap
brew install codemap
```

### Scoop (Windows)

```powershell
scoop bucket add codemap https://github.com/JordanCoin/scoop-codemap
scoop install codemap
```

### Winget (Windows)

```powershell
winget install JordanCoin.codemap
```

> **Note:** Winget availability depends on Microsoft approval. Use Scoop if not yet available.

### Download Binary

Pre-built binaries are available for all platforms on the [Releases page](https://github.com/JordanCoin/codemap/releases):

- **macOS**: `codemap-darwin-amd64.tar.gz` (Intel) or `codemap-darwin-arm64.tar.gz` (Apple Silicon)
- **Linux**: `codemap-linux-amd64.tar.gz` or `codemap-linux-arm64.tar.gz`
- **Windows**: `codemap-windows-amd64.zip`

```bash
# Example: download and install on Linux/macOS
curl -L https://github.com/JordanCoin/codemap/releases/latest/download/codemap-linux-amd64.tar.gz | tar xz
sudo mv codemap-linux-amd64/codemap /usr/local/bin/
```

> **Note:** The `--deps` feature requires [ast-grep](https://ast-grep.github.io/). Install via `brew install ast-grep`, `pip install ast-grep-cli`, or `cargo install ast-grep`.

### From source

```bash
git clone https://github.com/JordanCoin/codemap.git
cd codemap
go build -o codemap .
```

## Usage

Run `codemap` in any directory:

```bash
codemap
```

Or specify a path:

```bash
codemap /path/to/my/project
```

### AI Usage Example

**The Killer Use Case:**

1.  Run codemap and copy the output:
    ```bash
    codemap . | pbcopy
    ```

2.  Or simply tell Claude, Codex, or Cursor:
    > "Use codemap to understand my project structure."

## Diff Mode

See what you're working on with `--diff`:

```bash
codemap --diff
```

```
╭─────────────────────────── myproject ──────────────────────────╮
│ Changed: 4 files | +156 -23 lines vs main                      │
│ Top Extensions: .go (3), .tsx (1)                              │
╰────────────────────────────────────────────────────────────────╯
myproject
├── api/
│   └── (new) auth.go         ✎ handlers.go (+45 -12)
├── web/
│   └── ✎ Dashboard.tsx (+82 -8)
└── ✎ main.go (+29 -3)

⚠ handlers.go is used by 3 other files
⚠ api is used by 2 other files
```

**What it shows:**
- 📊 **Change summary**: Total files and lines changed vs main branch
- ✨ **New vs modified**: `(new)` for untracked files, `✎` for modified
- 📈 **Line counts**: `(+45 -12)` shows additions and deletions per file
- ⚠️ **Impact analysis**: Which changed files are imported by others

Compare against a different branch:
```bash
codemap --diff --ref develop
```

## Dependency Flow Mode

See how your code connects with `--deps`:

```bash
codem