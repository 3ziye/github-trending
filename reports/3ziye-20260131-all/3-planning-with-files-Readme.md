# Planning with Files

> **Work like Manus** — the AI agent company Meta acquired for **$2 billion**.

## Thank You

To everyone who starred, forked, and shared this skill — thank you. This project blew up in less than 24 hours, and the support from the community has been incredible.

If this skill helps you work smarter, that's all I wanted.

---

A Claude Code plugin that transforms your workflow to use persistent markdown files for planning, progress tracking, and knowledge storage — the exact pattern that made Manus worth billions.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-blue)](https://code.claude.com/docs/en/plugins)
[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-green)](https://code.claude.com/docs/en/skills)
[![Cursor Skills](https://img.shields.io/badge/Cursor-Skills-purple)](https://docs.cursor.com/context/skills)
[![Kilocode Skills](https://img.shields.io/badge/Kilocode-Skills-orange)](https://kilo.ai/docs/agent-behavior/skills)
[![Gemini CLI](https://img.shields.io/badge/Gemini%20CLI-Skills-4285F4)](https://geminicli.com/docs/cli/skills/)
[![Moltbot](https://img.shields.io/badge/Moltbot-Skills-FF6B6B)](https://docs.molt.bot/tools/skills)
[![Kiro](https://img.shields.io/badge/Kiro-Steering-00D4AA)](https://kiro.dev/docs/cli/steering/)
[![AdaL CLI](https://img.shields.io/badge/AdaL%20CLI-Skills-9B59B6)](https://docs.sylph.ai/features/plugins-and-skills)
[![Version](https://img.shields.io/badge/version-2.13.0-brightgreen)](https://github.com/OthmanAdi/planning-with-files/releases)
[![SkillCheck Validated](https://img.shields.io/badge/SkillCheck-Validated-4c1)](https://getskillcheck.com)

## Quick Install

```bash
# Install the plugin
claude plugins install OthmanAdi/planning-with-files
```

That's it! Now use one of these commands in Claude Code:

| Command | Autocomplete | Description |
|---------|--------------|-------------|
| `/planning-with-files:plan` | Type `/plan` | Shorter command (v2.11.0+) |
| `/planning-with-files:start` | Type `/planning` | Original command |

**Alternative:** If you want `/planning-with-files` (without prefix), copy skills to your local folder:

```bash
# Optional: Copy skills for /planning-with-files command
cp -r ~/.claude/plugins/cache/planning-with-files/planning-with-files/*/skills/planning-with-files ~/.claude/skills/
```

**Windows (PowerShell):**
```powershell
# Install the plugin
claude plugins install OthmanAdi/planning-with-files

# Optional: Copy skills for /planning-with-files command
Copy-Item -Recurse -Path "$env:USERPROFILE\.claude\plugins\cache\planning-with-files\planning-with-files\*\skills\planning-with-files" -Destination "$env:USERPROFILE\.claude\skills\"
```

See [docs/installation.md](docs/installation.md) for all installation methods.

## Supported IDEs

| IDE | Status | Installation Guide | Format |
|-----|--------|-------------------|--------|
| Claude Code | ✅ Full Support | [Installation](docs/installation.md) | Plugin + SKILL.md |
| Gemini CLI | ✅ Full Support | [Gemini Setup](docs/gemini.md) | Agent Skills |
| Moltbot | ✅ Full Support | [Moltbot Setup](docs/moltbot.md) | Workspace/Local Skills |
| Kiro | ✅ Full Support | [Kiro Setup](docs/kiro.md) | Steering Files |
| Cursor | ✅ Full Support | [Cursor Setup](docs/cursor.md) | Skills |
| Continue | ✅ Full Support | [Continue Setup](docs/continue.md) | Skills + Prompt files |
| Kilocode | ✅ Full Support | [Kilocode Setup](docs/kilocode.md) | Skills |
| OpenCode | ✅ Full Support | [OpenCode Setup](docs/opencode.md) | Personal/Project Skill |
| Codex | ✅ Full Support | [Codex Setup](docs/codex.md) | Personal Skill |
| FactoryAI Droid | ✅ Full Support | [Factory Setup](docs/factory.md) | Workspace/Personal Skill |
| Antigravity | ✅ Full Support | [Antigravity Setup](docs/antigravity.md) | Workspace/Personal Skill |
| CodeBuddy | ✅ Full Support | [CodeBuddy Setup](docs/codebuddy.md) | Workspace/Personal Skill |
| AdaL CLI (Sylph AI) | ✅ Full Support | [AdaL Setup](docs/adal.md) | Personal/Project Skills |

> **Note:** If your IDE uses the legacy Rules system instead of Skills, see the [`legacy-rules-support`](https://github.com/OthmanAdi/planning-with-files/tree/legacy-rules-support) branch.

## Documentation

| Document | Description |
|----------|-------------|
| [Installation Guide](docs/installation.md) | All installation methods (plugin, manual, Cursor, Windows) |
| [Quick Start](docs/quickstart.md) | 5-step guide to using the pattern |
| [Workflow Diagram](docs/workflow.md) | Visual diagram of how files and hooks interact |
| [Troubleshooting](docs/troubleshooting.md) | Common issues and solutions |
| [Gemini CLI Setup](docs/gemini.md) | Google Gemini CLI integration guide |
| [Moltbot Setup](docs/moltbot.md) | Moltbot integration guide |
| [Kiro Setup](docs/kiro.md) | Kiro steering files integration |
| [Cursor Setup](docs/c