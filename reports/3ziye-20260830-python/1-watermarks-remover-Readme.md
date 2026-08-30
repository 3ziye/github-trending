```
_ _ _ ____ ___ ____ ____ _  _ ____ ____ _  _ ____    ____ ____ _  _ ____ _  _ ____ ____
| | | |__|  |  |___ |__/ |\/| |__| |__/ |_/  [__  __ |__/ |___ |\/| |  | |  | |___ |__/
|_|_| |  |  |  |___ |  \ |  | |  | |  \ | \_ ___]    |  \ |___ |  | |__|  \/  |___ |  \
```

# watermarks-remover

<!-- logo: figlet -d .figlet -f cybermedium -w 120 "watermarks-remover" -->

[![CI](https://github.com/guillaumemeyer/watermarks-remover/actions/workflows/ci.yml/badge.svg)](https://github.com/guillaumemeyer/watermarks-remover/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/guillaumemeyer/watermarks-remover)](https://github.com/guillaumemeyer/watermarks-remover/releases)
[![Stars](https://img.shields.io/github/stars/guillaumemeyer/watermarks-remover)](https://github.com/guillaumemeyer/watermarks-remover/stargazers)
[![Forks](https://img.shields.io/github/forks/guillaumemeyer/watermarks-remover)](https://github.com/guillaumemeyer/watermarks-remover/forks)

Agent skill + stdlib Python service to strip **multi-vendor AI provenance marks** from text and files — for privacy and hygiene on content **you own**. The skill is a thin client: it drives the machinery over HTTP, so the agent host needs no Python.

| Layer | Target | How |
| --- | --- | --- |
| **A** | Invisible Unicode, exotic spaces, bidi, tag chars | Deterministic Python scripts |
| **B** | Statistical (token-sampling) text watermarks | Agent rewrite + optional `rewrite_text.py` hook |
| **Files** | C2PA / EXIF / XMP / doc props | PNG, JPEG, WebP, AVIF, HEIC, BMP, GIF, TIFF, SVG, PDF, DOCX, XLSX, PPTX, EPUB, ODT, HTML, Markdown, MP4/MOV/M4A/M4V, WAV, MP3, FLAC |

Vendors / ecosystems (class-level): **Claude**, **Gemini / SynthID-Text**, **OpenAI** provenance surfaces, **open-LLM** Kirchenbauer-style (green-list) and keyed-Gumbel / EXP (Aaronson) marks.

**Latest release:** [v0.6.0](https://github.com/guillaumemeyer/watermarks-remover/releases/tag/v0.6.0)

Skill path: [`skills/remove-ai-marks/`](skills/remove-ai-marks/)  
Service path: [`service/`](service/)  
(migration: formerly `remove-claude-marks`; slash alias `/remove-claude-marks` still documented)

## Install (agent skill)

The skill ships **no code** — it calls the service over HTTP. Install the skill (markdown only) and start the service, then set `WATERMARKS_SERVICE_URL` if it is not `http://127.0.0.1:8765`.

In Claude Code, the fastest route is the bundled
[plugin marketplace](#claude-code-plugin-marketplace) — no clone, and it updates
in place. Everywhere else, one installer covers every supported host
(Python 3.10+ stdlib, no dependencies):

```bash
python3 install_skill.py --skill remove-ai-marks --target claude-code
```

| Host | Target | Lands in |
| --- | --- | --- |
| Claude Code (personal) | `--target claude-code` | `~/.claude/skills/<skill>` (honors `CLAUDE_CONFIG_DIR`) |
| Claude Code (project) | `--target claude-project --project-dir PATH` | `PATH/.claude/skills/<skill>` |
| Cowork, claude.ai, cloud sessions, routines | `--target cowork` | `dist/<skill>.zip` to upload under **Customize → Skills** |
| Cursor | `--target cursor` (default) | `~/.cursor/skills/<skill>` |

Shipped skills: `remove-ai-marks` (full, service-backed) and
`clean-user-facing-text` (text only, self-contained). `--list` prints them.
Existing installations are preserved unless you pass `--force`; replacement is
staged first and the previous install is kept as a uniquely named backup.
`--link` symlinks this checkout instead of copying, so edits are picked up
live. On Windows, use `py install_skill.py ...`; the `install-skill.sh` wrapper
is provided for macOS/Linux shells.

Before writing anything, the installer validates the skill against the
[Agent Skills](https://agentskills.io) packaging rules that claude.ai uploads
and the Skills API enforce: spec-only frontmatter (`name`, `description`,
`license`, `compatibility`, `metadata`, `allowed-tools`), a lowercase hyphenated
`name` of at most 64 characters matching the directory, a non-empty
`description` of at most 1024 characters. The Cowork bundle additionally has
to fit the 30 MB upload limit, which the packager enforces.

### Automatic cleaning via hook (deterministic)

A skill is an instruction: the model decides whether to invoke it, and the
model is the thing producing the marks. A **hook** is executed by the harness
on every matching tool call, cooperation not required. That makes the hook the
deterministic half of this workflow.

The plugin registers a `PostToolUse` hook on `Write|Edit|MultiEdit|NotebookEdit`
that runs [`service/scripts/hook_written_file.py`](service/scripts/hook_written_file.py)
against the file the agent just wrote. Two modes, matching the pre-commit
convention of check-by-default:

| Mode | Behaviour |
| --- | --- |
| `check` (default) | Reports provenance marks, leaves the file alone. Findings go to the model (exit 2), so it can offer to clean them. |
| `clean` | Strips the marks in place, then tells the model the fi