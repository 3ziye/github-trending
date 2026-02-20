# rtk - Rust Token Killer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**High-performance CLI proxy to minimize LLM token consumption.**

[Website](https://www.rtk-ai.app) | [GitHub](https://github.com/rtk-ai/rtk) | [Install](INSTALL.md)

rtk filters and compresses command outputs before they reach your LLM context, saving 60-90% of tokens on common operations.

## ⚠️ Important: Name Collision Warning

**There are TWO different projects named "rtk":**

1. ✅ **This project (Rust Token Killer)** - LLM token optimizer
   - Repos: `rtk-ai/rtk`
   - Purpose: Reduce Claude Code token consumption

2. ❌ **reachingforthejack/rtk** - Rust Type Kit (DIFFERENT PROJECT)
   - Purpose: Query Rust codebase and generate types
   - **DO NOT install this one if you want token optimization**

**How to verify you have the correct rtk:**
```bash
rtk --version   # Should show "rtk 0.20.1"
rtk gain        # Should show token savings stats
```

If `rtk gain` doesn't exist, you installed the wrong package. See installation instructions below.

## Token Savings (30-min Claude Code Session)

Typical session without rtk: **~150,000 tokens**
With rtk: **~45,000 tokens** → **70% reduction**

| Operation | Frequency | Standard | rtk | Savings |
|-----------|-----------|----------|-----|---------|
| `ls` / `tree` | 10× | 2,000 | 400 | -80% |
| `cat` / `read` | 20× | 40,000 | 12,000 | -70% |
| `grep` / `rg` | 8× | 16,000 | 3,200 | -80% |
| `git status` | 10× | 3,000 | 600 | -80% |
| `git diff` | 5× | 10,000 | 2,500 | -75% |
| `git log` | 5× | 2,500 | 500 | -80% |
| `git add/commit/push` | 8× | 1,600 | 120 | -92% |
| `npm test` / `cargo test` | 5× | 25,000 | 2,500 | -90% |
| `ruff check` | 3× | 3,000 | 600 | -80% |
| `pytest` | 4× | 8,000 | 800 | -90% |
| `go test` | 3× | 6,000 | 600 | -90% |
| `docker ps` | 3× | 900 | 180 | -80% |
| **Total** | | **~118,000** | **~23,900** | **-80%** |

> Estimates based on medium-sized TypeScript/Rust projects. Actual savings vary by project size.

## Installation

### ⚠️ Pre-Installation Check (REQUIRED)

**ALWAYS verify if rtk is already installed before installing:**

```bash
rtk --version        # Check if installed
rtk gain             # Verify it's the Token Killer (not Type Kit)
which rtk            # Check installation path
```

If already installed and `rtk gain` works, **DO NOT reinstall**. Skip to Quick Start.

### Homebrew (macOS/Linux)

```bash
brew install rtk
```

### Quick Install (Linux/macOS)

```bash
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh
```

> **Note**: rtk installs to `~/.local/bin` by default. If this directory is not in your PATH, add it:
> ```bash
> echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc  # or ~/.zshrc
> ```

After installation, **verify you have the correct rtk**:
```bash
rtk gain  # Must show token savings stats (not "command not found")
```

### Alternative: Manual Installation

```bash
# From rtk-ai upstream (maintained by pszymkowiak)
cargo install --git https://github.com/rtk-ai/rtk

# OR if published to crates.io
cargo install rtk
```

⚠️ **WARNING**: `cargo install rtk` from crates.io might install the wrong package (Type Kit instead of Token Killer). Always verify with `rtk gain` after installation.

### Alternative: Pre-built Binaries

Download from [rtk-ai/releases](https://github.com/rtk-ai/rtk/releases):
- macOS: `rtk-x86_64-apple-darwin.tar.gz` / `rtk-aarch64-apple-darwin.tar.gz`
- Linux: `rtk-x86_64-unknown-linux-gnu.tar.gz` / `rtk-aarch64-unknown-linux-gnu.tar.gz`
- Windows: `rtk-x86_64-pc-windows-msvc.zip`

## Quick Start

```bash
# 1. Verify installation
rtk gain  # Must show token stats, not "command not found"

# 2. Initialize for Claude Code (RECOMMENDED: hook-first mode)
rtk init --global
# → Installs hook + creates slim RTK.md (10 lines, 99.5% token savings)
# → Follow printed instructions to add hook to ~/.claude/settings.json

# 3. Test it works
rtk git status  # Should show ultra-compact output
rtk init --show # Verify hook is installed and executable

# Alternative modes:
# rtk init --global --claude-md  # Legacy: full injection (137 lines)
# rtk init                       # Local project only (./CLAUDE.md)
```

**New in v0.9.5**: Hook-first installation eliminates ~2000 tokens from Claude's context while maintaining full RTK functionality through transparent command rewriting.

## Global Flags

```bash
-u, --ultra-compact    # ASCII icons, inline format (extra token savings)
-v, --verbose          # Increase verbosity (-v, -vv, -vvv)
```

## Commands

### Files
```bash
rtk ls .                        # Token-optimized directory tree
rtk read file.rs                # Smart file reading
rtk read file.rs -l aggressive  # Signatures only (strips bodies)
rtk smart file.rs               # 2-line heuristic code summary
rtk find "*.rs" .               # Compact find results
rtk grep "pattern" .            # Grouped search results
