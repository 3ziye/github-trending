<p align="center">
  <a href="https://github.com/travisvn/awesome-claude-skills">
    <img alt="Awesome Claude Skills" src="https://pc0o4oduww.ufs.sh/f/crfz5GypRfo0lI4924gMSJKLY6297aVP0zZpilXBvqTbDyrs"/>
  </a>
</p>

# Awesome Claude Skills

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Last Updated](https://img.shields.io/badge/updated-Oct%202025-green.svg)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License](https://img.shields.io/badge/license-CC0--1.0-blue.svg)](LICENSE)

> A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**Claude Skills** teach Claude how to **perform tasks in a repeatable way**

They are specialized folders containing instructions, scripts, and resources.

## 🚀 Quick Start

### Claude Code

```bash
/plugin marketplace add anthropics/skills
```

### Claude Desktop

[Enable Skills here](https://claude.ai/settings/capabilities)

## 🛠️ Installation & Setup

### Claude.ai Web Interface

1. Go to [Settings > Capabilities](https://claude.ai/settings/capabilities)
2. Enable Skills toggle
3. Browse available skills or upload custom skills
4. **For Team/Enterprise**: Admin must enable Skills organization-wide first

### Claude Code CLI

```bash
# Install skills from marketplace
/plugin marketplace add anthropics/skills

# Or install from local directory
/plugin add /path/to/skill-directory
```

### Claude API

Skills are accessible via the `/v1/skills` API endpoint. See the [Skills API documentation](https://docs.claude.com/en/api/skills) for detailed integration examples.

```python
import anthropic

client = anthropic.Client(api_key="your-api-key")
# See API docs for full implementation details
```

## 🎯 Official Skills

### Document Skills

Skills for working with complex file formats:

- **[docx](https://github.com/anthropics/skills/tree/main/document-skills/docx)** - Create, edit, and analyze Word documents with support for tracked changes, comments, formatting preservation, and text extraction
- **[pdf](https://github.com/anthropics/skills/tree/main/document-skills/pdf)** - Comprehensive PDF manipulation toolkit for extracting text and tables, creating new PDFs, merging/splitting documents, and handling forms
- **[pptx](https://github.com/anthropics/skills/tree/main/document-skills/pptx)** - Create, edit, and analyze PowerPoint presentations with support for layouts, templates, charts, and automated slide generation
- **[xlsx](https://github.com/anthropics/skills/tree/main/document-skills/xlsx)** - Create, edit, and analyze Excel spreadsheets with support for formulas, formatting, data analysis, and visualization

### Design & Creative

- **[algorithmic-art](https://github.com/anthropics/skills/tree/main/algorithmic-art)** - Create generative art using p5.js with seeded randomness, flow fields, and particle systems
- **[canvas-design](https://github.com/anthropics/skills/tree/main/canvas-design)** - Design beautiful visual art in .png and .pdf formats using design philosophies
- **[slack-gif-creator](https://github.com/anthropics/skills/tree/main/slack-gif-creator)** - Create animated GIFs optimized for Slack's size constraints

### Development

- **[artifacts-builder](https://github.com/anthropics/skills/tree/main/artifacts-builder)** - Build complex claude.ai HTML artifacts using React, Tailwind CSS, and shadcn/ui components
- **[mcp-builder](https://github.com/anthropics/skills/tree/main/mcp-builder)** - Guide for creating high-quality MCP servers to integrate external APIs and services
- **[webapp-testing](https://github.com/anthropics/skills/tree/main/webapp-testing)** - Test local web applications using Playwright for UI verification and debugging

### Communication

- **[brand-guidelines](https://github.com/anthropics/skills/tree/main/brand-guidelines)** - Apply Anthropic's official brand colors and typography to artifacts
- **[internal-comms](https://github.com/anthropics/skills/tree/main/internal-comms)** - Write internal communications like status reports, newsletters, and FAQs

### Skill Creation

- **[skill-creator](https://github.com/anthropics/skills/tree/main/skill-creator)** - Interactive skill creation tool that guides you through building new skills with Q&A

## 🌟 Community Skills

> [!Warning]
> Skills can execute arbitrary code in Claude's environment.
> 
> See [Security & Best Practices](#-security--best-practices) for more information

### Collections & Libraries

- **[obra/superpowers](https://github.com/obra/superpowers)** - Core skills library for Claude Code with 20+ battle-tested skills including TDD, debugging, and collaboration patterns
  - Features `/brainstorm`, `/write-plan`, `/execute-plan` commands and skills-search tool
  - [superpowers-skills](https://github.com/obra/superpowers-skills) - Community-editable skills repository
  - [Blog: Superpowers](https://blog.fsck.com/2025/10/09/superpowers/) - Author's overview by Jesse Vincent
