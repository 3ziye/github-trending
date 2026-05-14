# Reversa 
<small>by sandeco</small>

**Turn legacy systems into executable specifications for AI agents.**

[![English Docs](https://img.shields.io/badge/DOCS-English-009c3b?style=for-the-badge&logo=material-for-mkdocs&logoColor=white&labelColor=2d2d2d)](https://sandeco.github.io/reversa/)<br>
[![Português Docs](https://img.shields.io/badge/DOCS-Portugu%C3%AAs-ffcc00?style=for-the-badge&logo=material-for-mkdocs&logoColor=black&labelColor=2d2d2d)](https://sandeco.github.io/reversa/pt/)<br>
[![Español Docs](https://img.shields.io/badge/DOCS-Espa%C3%B1ol-c60b1e?style=for-the-badge&logo=material-for-mkdocs&logoColor=white&labelColor=2d2d2d)](https://sandeco.github.io/reversa/es/)

Reversa is a specification reverse-engineering framework. Install it inside a legacy project and it coordinates a team of specialized AI agents to analyze the existing code and generate complete, traceable specifications ready for use by any coding agent.

---

## Why Reversa exists

Most production systems carry years of accumulated knowledge: implicit business rules, undocumented architectural decisions, critical logic buried in code nobody wants to touch. That knowledge exists, but it's trapped.

AI agents are transformative for creating and evolving software, but they depend on specifications to operate safely. For new systems, you write the spec and the agent executes. For legacy systems — or those built with pure vibe coding — there is no spec: the agent has no way of knowing what it cannot break.

**Reversa is the bridge between the legacy system and AI agents.**

It analyzes the existing code, extracts accumulated knowledge (business rules, flows, module contracts, retroactive architectural decisions) and transforms everything into executable, traceable specifications ready for any coding agent.

The result is not documentation for humans to read. These are **operational contracts** that allow an agent to evolve the system with fidelity to what already exists.

---

## Installation

In the root of the legacy project:

```bash
npx reversa install
```

The installer will:
1. Detect the AI engines present in the environment (Claude Code, Codex, Cursor, etc.)
2. Ask which agents to install — all selected by default
3. Collect project name, language, and preferences
4. Copy agents to `.agents/skills/` (and `.claude/skills/` for Claude Code)
5. Create the engine entry file (`CLAUDE.md`, `AGENTS.md`, etc.)
6. Create the `.reversa/` structure with state, configuration, and plan
7. Generate SHA-256 manifest for safe updates

> Reversa **never deletes or modifies** existing files in your project.
> Agents write only to `.reversa/` and the output folder (`_reversa_sdd/` by default).

**Requirements:** Node.js 18+

---

> [!IMPORTANT]
> ### 🔒 Guaranteed immutability of the legacy project
>
> The installer only creates new files (`CLAUDE.md`, `AGENTS.md`, `.agents/skills/`, etc.) and **never modifies or deletes any existing file** in your project. During analysis, agents operate under a strict and inviolable directive: **all writes are restricted to `.reversa/` and `_reversa_sdd/`** — no other file in your project is touched.

> [!CAUTION]
> ### 💾 Back up your project before starting
>
> Although Reversa never modifies your files, AI agents can make mistakes. **We strongly recommend:**
>
> 1. **Version the project in Git** — make sure all files are committed before starting the analysis
> 2. **Have the repository on GitHub** (or GitLab, Bitbucket) — so you have a safe remote copy
> 3. **Make a local copy of the folder** — a simple `cp -r my-project my-project-backup` protects against any unexpected event
>
> If something unexpected happens during analysis, you can restore the original state with `git restore .` or from the backup copy.

> [!WARNING]
> 🔑 **Reversa does not request, store, or transmit API keys from any LLM service.** All intelligence is delegated to the AI agent already present in your environment (Claude Code, Codex, Cursor, etc.) — no external authentication dependencies.

---

## How to use

After installation, open the project in the AI agent and activate Reversa:

```
/reversa
```

For engines without slash command support (like Codex):

```
reversa
```

Reversa will introduce itself, create a personalized exploration plan, and coordinate the entire analysis. Progress is saved in `.reversa/state.json` at each checkpoint — if the session is interrupted, just type `reversa` to resume where you left off.

---

## How it works

Reversa uses a 5-phase pipeline orchestrated by the **Reversa** agent:

```
Reconnaissance  Excavation  Interpretation  Generation  Review
    Scout       Archaeologist  Detective      Writer    Reviewer
                                Architect
```

Independent agents (run at any phase): **Visor**, **Data Master**, **Design System**, **Tracer**

---

## Agents

### Required

| Agent | Role |
|-------|------|
| **Reversa** | Central orchestrator. Coordinates all agents, saves checkpoints, guides the