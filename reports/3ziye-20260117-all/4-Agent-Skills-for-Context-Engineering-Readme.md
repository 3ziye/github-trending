# Agent Skills for Context Engineering

A comprehensive, open collection of Agent Skills focused on context engineering principles for building production-grade AI agent systems. These skills teach the art and science of curating context to maximize agent effectiveness across any agent platform.

## What is Context Engineering?

Context engineering is the discipline of managing the language model's context window. Unlike prompt engineering, which focuses on crafting effective instructions, context engineering addresses the holistic curation of all information that enters the model's limited attention budget: system prompts, tool definitions, retrieved documents, message history, and tool outputs.

The fundamental challenge is that context windows are constrained not by raw token capacity but by attention mechanics. As context length increases, models exhibit predictable degradation patterns: the "lost-in-the-middle" phenomenon, U-shaped attention curves, and attention scarcity. Effective context engineering means finding the smallest possible set of high-signal tokens that maximize the likelihood of desired outcomes.

## Skills Overview

### Foundational Skills

These skills establish the foundational understanding required for all subsequent context engineering work.

| Skill | Description |
|-------|-------------|
| [context-fundamentals](skills/context-fundamentals/) | Understand what context is, why it matters, and the anatomy of context in agent systems |
| [context-degradation](skills/context-degradation/) | Recognize patterns of context failure: lost-in-middle, poisoning, distraction, and clash |
| [context-compression](skills/context-compression/) | Design and evaluate compression strategies for long-running sessions |

### Architectural Skills

These skills cover the patterns and structures for building effective agent systems.

| Skill | Description |
|-------|-------------|
| [multi-agent-patterns](skills/multi-agent-patterns/) | Master orchestrator, peer-to-peer, and hierarchical multi-agent architectures |
| [memory-systems](skills/memory-systems/) | Design short-term, long-term, and graph-based memory architectures |
| [tool-design](skills/tool-design/) | Build tools that agents can use effectively |
| [filesystem-context](skills/filesystem-context/) | Use filesystems for dynamic context discovery, tool output offloading, and plan persistence |
| [hosted-agents](skills/hosted-agents/) | **NEW** Build background coding agents with sandboxed VMs, pre-built images, multiplayer support, and multi-client interfaces |

### Operational Skills

These skills address the ongoing operation and optimization of agent systems.

| Skill | Description |
|-------|-------------|
| [context-optimization](skills/context-optimization/) | Apply compaction, masking, and caching strategies |
| [evaluation](skills/evaluation/) | Build evaluation frameworks for agent systems |
| [advanced-evaluation](skills/advanced-evaluation/) | Master LLM-as-a-Judge techniques: direct scoring, pairwise comparison, rubric generation, and bias mitigation |

### Development Methodology

These skills cover the meta-level practices for building LLM-powered projects.

| Skill | Description |
|-------|-------------|
| [project-development](skills/project-development/) | Design and build LLM projects from ideation through deployment, including task-model fit analysis, pipeline architecture, and structured output design |

### Cognitive Architecture Skills

These skills cover formal cognitive modeling for rational agent systems.

| Skill | Description |
|-------|-------------|
| [bdi-mental-states](skills/bdi-mental-states/) | **NEW** Transform external RDF context into agent mental states (beliefs, desires, intentions) using formal BDI ontology patterns for deliberative reasoning and explainability |

## Design Philosophy

### Progressive Disclosure

Each skill is structured for efficient context use. At startup, agents load only skill names and descriptions. Full content loads only when a skill is activated for relevant tasks.

### Platform Agnosticism

These skills focus on transferable principles rather than vendor-specific implementations. The patterns work across Claude Code, Cursor, and any agent platform that supports skills or allows custom instructions.

### Conceptual Foundation with Practical Examples

Scripts and examples demonstrate concepts using Python pseudocode that works across environments without requiring specific dependency installations.

## Usage

### Usage with Claude Code

This repository is a **Claude Code Plugin Marketplace** containing context engineering skills that Claude automatically discovers and activates based on your task context.

### Installation

**Step 1: Add the Marketplace**

Run this command in Claude Code to register this repository as a plugin source:

```
/plugin marketplace add muratcankoylan/Agent-Skills-for-Context-Engineering
```

**Step 2: Browse and Install**

Option A - Browse available 