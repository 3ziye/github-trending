# claude-replay

![npm](https://img.shields.io/npm/v/claude-replay)
![Claude Code](https://img.shields.io/badge/Claude_Code-replay-blue)
![Cursor](https://img.shields.io/badge/Cursor-replay-purple)
![Codex CLI](https://img.shields.io/badge/Codex_CLI-replay-green)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Node.js](https://img.shields.io/badge/node-18%2B-green.svg)
![Zero Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen)

> Community tool — not affiliated with or endorsed by Anthropic.

AI coding sessions are great for development, but hard to share. Screen recordings are bulky and transcripts are hard to navigate.

**claude-replay** turns Claude Code, Cursor, and Codex CLI session logs into interactive, shareable HTML replays. The generated replay is a single self-contained HTML file with no external dependencies — you can email it, host it anywhere, or embed it in documentation.

![Demo](https://raw.githubusercontent.com/es617/claude-replay/main/docs/demo.gif)

**[Try it online](https://es617.github.io/claude-replay/)** · **[Live demo](https://es617.github.io/claude-replay/demo-redaction.html)**

Claude Code, Cursor, and Codex CLI store conversation transcripts as JSONL files on disk. **claude-replay** auto-detects the format and converts them into visual replays suitable for blog posts, demos, and documentation.

| Source | Transcript location |
|---|---|
| Claude Code | `~/.claude/projects/<project>/` |
| Cursor | `~/.cursor/projects/<project>/agent-transcripts/<id>/` |
| Codex CLI | `~/.codex/sessions/<date>/` |

## Features

- Self-contained HTML output (no dependencies)
- Interactive playback with speed control
- Collapse/expand tool calls and thinking blocks (Claude's internal reasoning traces)
- Bookmarks / chapters
- Secret redaction before export
- Multiple color themes
- Terminal-style bottom-to-top scroll
- Embeddable via iframe
- Web-based editor UI for visual session editing and preview

## Use cases

claude-replay is useful for:

- **Blog posts** — show AI-assisted development sessions interactively
- **Documentation** — embed AI debugging sessions or code walkthroughs
- **Demos** — share reproducible sessions without video
- **Bug reports** — attach a replay instead of long logs
- **Teaching** — step through AI reasoning and tool usage

## Installation

```bash
npm install -g claude-replay
```

Or run directly with npx (zero install):

```bash
npx claude-replay
```

### Docker

```bash
docker run --rm -p 7331:7331 \
  -v ~/.claude/projects:/root/.claude/projects:ro \
  ghcr.io/es617/claude-replay
```

Open http://localhost:7331 for the web editor. Session directories are mounted read-only.

For CLI usage:

```bash
docker run --rm \
  -v ~/.claude/projects:/root/.claude/projects:ro \
  -v $(pwd):/output \
  ghcr.io/es617/claude-replay \
  /root/.claude/projects/my-project/session.jsonl -o /output/replay.html
```

## Quick start

```bash
# Launch the web editor (default)
claude-replay

# Generate a replay by session ID (auto-finds the file)
claude-replay abc123def456 -o replay.html

# Or pass the full path
claude-replay ~/.claude/projects/-Users-me-myproject/session-id.jsonl -o replay.html

# Chain multiple sessions into one replay
claude-replay session1-id session2-id -o combined.html
```

Running `claude-replay` with no arguments opens a browser-based editor that auto-discovers your Claude Code and Cursor sessions. From there you can browse, edit, preview, and export replays visually.

For CLI usage, you can pass just a session ID — claude-replay will search `~/.claude/projects/`, `~/.cursor/projects/`, and `~/.codex/sessions/` to find the matching file. Or pass the full path to a JSONL file directly.

### Cursor

Cursor transcripts are also supported — the format is auto-detected. Cursor transcripts don't include timestamps, so playback uses paced timing by default (see [Timing modes](#timing-modes)).

```bash
claude-replay ~/.cursor/projects/*/agent-transcripts/<id>/<id>.jsonl -o replay.html
```

### Codex CLI

Codex CLI (OpenAI) transcripts are also supported — the format is auto-detected. Codex tool calls (`exec_command`, `apply_patch`) are mapped to their Claude Code equivalents (`Bash`, `Edit`/`Write`) so they render with the same diff views and command previews.

```bash
claude-replay ~/.codex/sessions/2026/03/12/rollout-<id>.jsonl -o replay.html
```

## Web Editor

The default experience. Launch it by running `claude-replay` with no arguments:

```bash
claude-replay
claude-replay --port 8080
```

![Editor](https://raw.githubusercontent.com/es617/claude-replay/main/docs/editor-demo.gif)

The editor provides:
- **Session browser** — auto-discovers sessions from `~/.claude/projects/`, `~/.cursor/projects/`, and `~/.codex/sessions/`, plus a folder navigator for JSONL files stored elsewhere
- **Turn editor** — include/exclude turns, edit user prompts, expand assistant blocks (read-only), add bookmarks
- **Options panel** — theme, speed, thi