# Academic Research Skills for Codex

[![Version](https://img.shields.io/badge/version-v0.1.8-blue)](VERSION)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Sponsor](https://img.shields.io/badge/sponsor-Buy%20Me%20a%20Coffee-orange?logo=buy-me-a-coffee)](https://buymeacoffee.com/crucify020v)

Codex-native packaging of the Academic Research Skills suite. This is the
sibling Codex distribution of
[Academic Research Skills for Claude Code](https://github.com/Imbad0202/academic-research-skills).

This repository vendors the ARS workflow content as a single Codex skill:

```text
skills/academic-research-suite/
  SKILL.md
  manifest.json
  agents/openai.yaml
  ars/
    deep-research/
    academic-paper/
    academic-paper-reviewer/
    academic-pipeline/
    experiment-agent/
    commands/
    hooks/
    docs/
    tests/
    shared/
```

The original Claude Code ARS checkout is not modified. Upstream content is copied
from fresh GitHub clones and adapted through the Codex router in
`skills/academic-research-suite/SKILL.md`.

## Claude Code Version

This repository is the Codex package. For the original Claude Code version of
Academic Research Skills, use
[Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills).

Use the Claude Code repo when you want the native Claude Code skill layout,
Claude-specific agent-team behavior, or the original ARS development history.
Use this repo when you want the Codex-native single-suite skill.

## Versioning

This Codex package is version `0.1.8`. The repo-root `VERSION` file,
`skills/academic-research-suite/SKILL.md` metadata version, and
`skills/academic-research-suite/manifest.json` `adapter_version` track the
Codex package version independently of the vendored ARS suite. Vendored upstream
versions are recorded by commit in `manifest.source_repositories[]`.

Package-level changes are summarized in [`CHANGELOG.md`](CHANGELOG.md).

The vendored ARS source currently tracks
`Imbad0202/academic-research-skills@96b82e82142dc95f117595c207d3e150b078e411`
(`v3.9.4.2`). The v3.9.4.2 upstream delta is CI/release-gate-only under
`.github/`, which this Codex package intentionally excludes; vendored runtime
content includes ARS v3.9.4.1 temporal-verification hotfixes and the v3.9.1
through v3.9.4 workflow updates.

## Install Or Update

Install the skill from this repo path. Use `--method git` so public and
credentialed GitHub access both work consistently:

```bash
python "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo Imbad0202/academic-research-skills-codex \
  --ref main \
  --path skills/academic-research-suite \
  --method git
```

To update an existing install:

```bash
rm -rf "$HOME/.codex/skills/academic-research-suite"
python "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo Imbad0202/academic-research-skills-codex \
  --ref main \
  --path skills/academic-research-suite \
  --method git
```

Open a new Codex conversation after installation. Existing Codex sessions may
keep their old skill cache; you do not need to close unrelated Claude or Codex
sessions.

Verify with `/skills`: you should see one ARS entry, `academic-research-suite`
or `Academic Research ...`. You should **not** see separate `academic-paper`,
`academic-pipeline`, `deep-research`, or `academic-paper-reviewer` skills from
this package. If you do, reinstall with the update command above and open a new
Codex conversation.

## Codex Docs

- [Codex setup](skills/academic-research-suite/ars/docs/SETUP.md) covers
  installation, `ars-*` aliases, optional tools, Material Passport adapters,
  and unsupported Claude plugin features.
- [Codex architecture](skills/academic-research-suite/ars/docs/ARCHITECTURE.md)
  explains the logical ARS pipeline with the Codex runtime overlay.

## Usage

Invoke the suite explicitly with `$academic-research-suite` (singular), then
describe the research task and provide any source files, notes, draft text,
reviewer comments, or output constraints.

```text
Use $academic-research-suite to help me plan a systematic literature review on
AI adoption in higher education quality assurance.
```

The Codex adapter routes the request to one of five ARS workflows:

| Workflow | Use when you need | Example prompt |
|---|---|---|
| `deep-research` | Research question refinement, literature review, systematic review, meta-analysis, fact-checking | `Use $academic-research-suite to build a systematic review protocol for AI in higher education QA.` |
| `academic-paper` | Paper outline, drafting, abstract, revision, citation formatting, AI disclosure | `Use $academic-research-suite to turn these notes into an IMRaD paper outline and drafting plan.` |
| `academic-paper-reviewer` | Manuscript review, simulated peer review, editorial decision, re-review | `Use $academic-research-suite to rev