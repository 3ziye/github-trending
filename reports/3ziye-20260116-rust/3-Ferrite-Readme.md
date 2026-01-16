# Ferrite

<div align="center">

[![Latest Release](https://img.shields.io/github/v/release/OlaProeis/Ferrite?style=flat-square)](https://github.com/OlaProeis/Ferrite/releases)
[![License](https://img.shields.io/github/license/OlaProeis/Ferrite?style=flat-square)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/OlaProeis/Ferrite?style=flat-square)](https://github.com/OlaProeis/Ferrite/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/OlaProeis/Ferrite?style=flat-square)](https://github.com/OlaProeis/Ferrite/issues)
[![Build Status](https://img.shields.io/github/actions/workflow/status/OlaProeis/Ferrite/release.yml?branch=master&style=flat-square)](https://github.com/OlaProeis/Ferrite/actions)

</div>

A fast, lightweight text editor for Markdown, JSON, YAML, and TOML files. Built with Rust and egui for a native, responsive experience.

> ⚠️ **Platform Note:** Ferrite has been primarily developed and tested on **Windows**. While it should work on Linux and macOS, these platforms have not been extensively tested. If you encounter issues, please [report them](https://github.com/OlaProeis/Ferrite/issues).

## 🤖 AI-Assisted Development

This project is 100% AI-generated code. All Rust code, documentation, and configuration was written by Claude (Anthropic) via [Cursor](https://cursor.com) with MCP tools.

<details>
<summary><strong>About the AI workflow</strong></summary>

### My Role
- **Product direction** — Deciding what to build and why
- **Testing** — Running the app, finding bugs, verifying features
- **Review** — Reading generated code, understanding what it does
- **Orchestration** — Managing the AI workflow effectively

### The Workflow
1. **Idea refinement** — Discuss concepts with multiple AIs (Claude, Perplexity, Gemini Pro)
2. **PRD creation** — Generate requirements using [Task Master](https://github.com/task-master-ai/task-master)
3. **Task execution** — Claude Opus handles implementation (preferring larger tasks over many subtasks)
4. **Session handover** — Structured prompts maintain context between sessions
5. **Human review** — Every handover is reviewed; direction adjustments made as needed

📖 **Full details:** [AI Development Workflow](docs/ai-workflow/ai-development-workflow.md)

### Open Process
The actual prompts and documents used to build Ferrite are public:

| Document | Purpose |
|----------|---------|
| [`current-handover-prompt.md`](docs/current-handover-prompt.md) | Active session context |
| [`ai-workflow/`](docs/ai-workflow/) | Full workflow docs, PRDs, historical handovers |
| [`handover/`](docs/handover/) | Reusable handover templates |

This transparency is intentional — I want others to learn from (and improve upon) this approach.

</details>

## Screenshots

![Ferrite Demo](assets/screenshots/demo.gif)

| Raw Editor | Split View | Zen Mode |
|------------|------------|----------|
| ![Raw Editor](assets/screenshots/raw-dark.png) | ![Split View](assets/screenshots/split-dark.png) | ![Zen Mode](assets/screenshots/zen-dark.png) |

> ✨ **v0.2.3 Released:** Editor productivity features! Go to Line (Ctrl+G), Duplicate Line (Ctrl+Shift+D), Move Line (Alt+↑/↓), Auto-close brackets/quotes, Smart Paste for links, and configurable line width. See [CHANGELOG.md](CHANGELOG.md) for full details.

## Features

### Core Editing
- **WYSIWYG Markdown Editing** - Edit markdown with live preview, click-to-edit formatting, and syntax highlighting
- **Multi-Format Support** - Native support for Markdown, JSON, YAML, and TOML files
- **Tree Viewer** - Hierarchical view for JSON/YAML/TOML with inline editing, expand/collapse, and path copying
- **Find & Replace** - Search with regex support and match highlighting
- **Go to Line (Ctrl+G)** - Quick navigation to specific line number
- **Undo/Redo** - Full undo/redo support per tab

### View Modes
- **Split View** - Side-by-side raw editor and rendered preview with resizable divider
- **Zen Mode** - Distraction-free writing with centered text column

### Editor Features
- **Syntax Highlighting** - Full-file syntax highlighting for 40+ languages (Rust, Python, JavaScript, Go, etc.)
- **Code Folding** - Fold detection with gutter indicators (▶/▼) for headings, code blocks, and lists (text hiding deferred to v0.3.0)
- **Minimap** - VS Code-style navigation panel with click-to-jump and search highlights
- **Bracket Matching** - Highlight matching brackets `()[]{}<>` and emphasis pairs `**` `__`
- **Auto-close Brackets & Quotes** - Type `(`, `[`, `{`, `"`, or `'` to get matching pair; selection wrapping supported
- **Duplicate Line (Ctrl+Shift+D)** - Duplicate current line or selection
- **Move Line Up/Down (Alt+↑/↓)** - Rearrange lines without cut/paste
- **Smart Paste for Links** - Select text then paste URL to create `[text](url)` markdown link
- **Auto-Save** - Configurable auto-save with temp-file safety
- **Line Numbers** - Optional line number gutter
- **Configurable Line Width** - Limit text width for readability (80/1