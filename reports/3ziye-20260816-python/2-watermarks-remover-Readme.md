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
| **Files** | C2PA / EXIF / XMP / doc props | PNG, JPEG, WebP, SVG, PDF, DOCX, ODT, HTML, Markdown |

Vendors / ecosystems (class-level): **Claude**, **Gemini / SynthID-Text**, **OpenAI** provenance surfaces, **open-LLM** Kirchenbauer-style marks.

**Latest release:** [v0.5.0](https://github.com/guillaumemeyer/watermarks-remover/releases/tag/v0.5.0)

Skill path: [`skills/remove-ai-marks/`](skills/remove-ai-marks/)  
Service path: [`service/`](service/)  
(migration: formerly `remove-claude-marks`; slash alias `/remove-claude-marks` still documented)

## Install (agent skill)

The skill ships **no code** — it calls the service over HTTP. Install the skill (markdown only) and start the service, then set `WATERMARKS_SERVICE_URL` if it is not `http://127.0.0.1:8765`.

```bash
# Grok Build / project-local
mkdir -p .grok/skills
ln -sfn "$(pwd)/skills/remove-ai-marks" .grok/skills/remove-ai-marks

# User-global Grok
mkdir -p ~/.grok/skills
ln -sfn "$(pwd)/skills/remove-ai-marks" ~/.grok/skills/remove-ai-marks
```

Invoke with `/remove-ai-marks` or ask to “strip AI watermarks / C2PA / Claude marks / SynthID-class text.”

### Optional Cursor text-only skill

[`skills/clean-user-facing-text/`](skills/clean-user-facing-text/) is a
self-contained Cursor skill for authorized manuscripts, documentation, and web
copy. It excludes image, C2PA, service, and external-model tooling.

Install it into `~/.cursor/skills/clean-user-facing-text`:

```bash
python3 install_skill.py
```

On Windows, use `py install_skill.py`. The `install-skill.sh` wrapper is
provided for macOS/Linux shells. Existing installations are preserved unless
you pass `--force`; replacement is staged first and the previous install is
kept as a uniquely named backup.

Skill invocation is model-selected. Projects that explicitly adopt this
workflow can also copy the optional rule:

```bash
mkdir -p /path/to/project/.cursor/rules
cp integrations/cursor/clean-user-facing-text.mdc \
  /path/to/project/.cursor/rules/clean-user-facing-text.mdc
```

For all projects, put the same instruction in Cursor **User Rules** instead.
Rules improve consistency but remain model instructions; Cursor does not expose
a deterministic pre-send filter for final chat responses.

### Start the service

The fastest path is a local HTTP server (Python 3.10+ stdlib only — no deps, no Docker):

```bash
make serve                 # http://127.0.0.1:8765
# or directly:
python3 service/scripts/server.py --host 127.0.0.1 --port 8765
```

For the whole infra (core + optional harness/heavy backends), see [Docker / compose](#docker--compose) below.

Optional system tools (auto-used when present — preinstalled in the core Docker image):

| Tool | Role |
| --- | --- |
| [`c2patool`](https://github.com/contentauth/c2pa-rs/tree/main/cli) | Inspect C2PA manifests |
| [`exiftool`](https://exiftool.org/) | Residual metadata strip (esp. **PDF**) |
| [`qpdf`](https://qpdf.sourceforge.io/) | Structural PDF rebuild — **required** for a real PDF strip (see below) |

Core scripts need **Python 3.10+** stdlib only. Layer B model calls are optional.

## Quick use (scripts)

```bash
SCRIPTS=service/scripts

# Unified inspect / clean
python3 "$SCRIPTS/inspect_file.py" draft.md
python3 "$SCRIPTS/clean_file.py" draft.md -o draft.cleaned.md
python3 "$SCRIPTS/clean_file.py" photo.png -o photo.cleaned.png
python3 "$SCRIPTS/clean_file.py" notes.docx -o notes.cleaned.docx

# Text Layer A
python3 "$SCRIPTS/inspect_text.py" draft.md
python3 "$SCRIPTS/clean_text.py"