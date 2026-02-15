<!--<p align="center">
<img src="assets/meme.png" alt="AI Coding Problems Meme" />
</p>-->

<p align="center">
<picture>
<source srcset="assets/trellis.png" media="(prefers-color-scheme: dark)">
<source srcset="assets/trellis.png" media="(prefers-color-scheme: light)">
<img src="assets/trellis.png" alt="Trellis Logo" width="500" style="image-rendering: -webkit-optimize-contrast; image-rendering: crisp-edges;">
</picture>
</p>

<p align="center">
<strong>All-in-one AI framework & toolkit for Claude Code, Cursor, iFlow & Codex</strong><br/>
<sub>Wild AI ships nothing.</sub>
</p>

<p align="center">
<a href="https://www.npmjs.com/package/@mindfoldhq/trellis"><img src="https://img.shields.io/npm/v/@mindfoldhq/trellis.svg?style=flat-square&color=blue" alt="npm version" /></a>
<a href="https://github.com/mindfold-ai/Trellis/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-FSL-green.svg?style=flat-square" alt="license" /></a>
<a href="https://github.com/mindfold-ai/Trellis/stargazers"><img src="https://img.shields.io/github/stars/mindfold-ai/Trellis?style=flat-square&color=yellow" alt="stars" /></a>
<a href="https://discord.com/invite/tWcCZ3aRHc"><img src="https://img.shields.io/badge/Discord-Join-7289DA?style=flat-square&logo=discord&logoColor=white" alt="Discord" /></a>
</p>

<p align="center">
<a href="#quick-start">Quick Start</a> •
<a href="#why-trellis">Why Trellis</a> •
<a href="#use-cases">Use Cases</a> •
<a href="#how-it-works">How It Works</a> •
<a href="#faq">FAQ</a>
</p>

## Why Trellis?

| Feature | Problem Solved |
| --- | --- |
| **Auto-Injection** | Required specs and workflows auto-inject into every conversation. Write once, apply forever |
| **Auto-updated Spec Library** | Best practices live in auto-updated spec files. The more you use it, the better it gets |
| **Parallel Sessions** | Run multiple agents in tandem - each in its own worktree |
| **Team Sync** | Share specs across your team. One person's best practice benefits everyone |
| **Session Persistence** | Work traces persist in your repo. AI remembers project context across sessions |

## Quick Start

```bash
# 1. Install globally
npm install -g @mindfoldhq/trellis@latest

# 2. Initialize in your project directory
trellis init -u your-name

# Or include iFlow CLI support
trellis init --iflow -u your-name

# Or include Codex skills support
trellis init --codex -u your-name

# 3. Start Claude Code and begin working
```

> `your-name` becomes your identifier and creates a personal workspace at `.trellis/workspace/your-name/`

<p align="center">
<img src="assets/info.png" alt="Trellis Initialization Example" />
</p>

## Use Cases

### Educating Your AI

Write your specs in Markdown. Trellis injects them into every AI session — no more repeating yourself.

<p align="center">
<img src="assets/usecase1.png" alt="Teaching AI - Teach Once, Apply Forever" />
</p>

Define your component guidelines, file structure rules, and patterns once. AI automatically applies them when creating new code — using TypeScript with Props interface, following PascalCase naming, building functional components with hooks.

### Ship in Parallel

Spawn multiple Claude sessions in isolated worktrees with `/trellis:parallel`. Work on several features at once, merge when ready.

<p align="center">
<img src="assets/usecase2.png" alt="Parallel Work - Multiple features developing simultaneously" />
</p>

While coding, each worker runs in its own worktree (physically isolated directory), no blocking, no interference. Review and merge completed features while others are still in progress.

### Custom Workflows

Define custom skills & commands that prepare Claude for specific tasks and contexts.

<p align="center">
<img src="assets/usecase3.png" alt="Workflows - Custom commands for instant context loading" />
</p>

Create commands like `/trellis:before-frontend-dev` that load component guidelines, check recent changes, pull in test patterns, and review shared hooks—all with a single slash.

## How It Works

### Project Structure

```
.trellis/
├── workflow.md              # Workflow guide (auto-injected on start)
├── worktree.yaml            # Multi-agent config (for /trellis:parallel)
├── spec/                    # Spec library
│   ├── frontend/            #   Frontend specs
│   ├── backend/             #   Backend specs
│   └── guides/              #   Decision & analysis frameworks
├── workspace/{name}/        # Personal journal
├── tasks/                   # Task management (progress tracking & more)
└── scripts/                 # Utilities

.claude/
├── settings.json            # Hook configuration
├── agents/                  # Agent definitions
│   ├── dispatch.md          #   Dispatch Agent (pure routing, doesn't read specs)
│   ├── implement.md         #   Implement Agent
│   ├── check.md             #   Check Agent
│   └── research.md          #   Research Agent
├── commands/                # Slash commands
└── hooks/                   # Hook scripts
 