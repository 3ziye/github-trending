# Claude Code Toolkit

**The most comprehensive toolkit for Claude Code -- 135 agents, 35 curated skills (+15,000 via [SkillKit](https://agenstskills.com)), 42 commands, 120 plugins, 19 hooks, 15 rules, 7 templates, 6 MCP configs, and more.**

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-Feb%202026-orange.svg)](#)
[![Files](https://img.shields.io/badge/Files-796-blueviolet.svg)](#project-structure)

---

## Quick Install

**Plugin marketplace** (recommended):

```bash
/plugin marketplace add rohitg00/awesome-claude-code-toolkit
```

**Manual clone:**

```bash
git clone https://github.com/rohitg00/awesome-claude-code-toolkit.git ~/.claude/plugins/claude-code-toolkit
```

**One-liner:**

```bash
curl -fsSL https://raw.githubusercontent.com/rohitg00/awesome-claude-code-toolkit/main/setup/install.sh | bash
```

---

## Table of Contents

- [Plugins](#plugins) (120)
- [Agents](#agents) (135)
- [Skills](#skills) (35)
- [Commands](#commands) (42)
- [Hooks](#hooks) (19 scripts)
- [Rules](#rules) (15)
- [Templates](#templates) (7)
- [MCP Configs](#mcp-configs) (6)
- [Contexts](#contexts) (5)
- [Examples](#examples) (3)
- [Setup](#setup)
- [Contributing](#contributing)

---

## Plugins

One hundred twenty production-ready plugins that extend Claude Code with domain-specific capabilities.

| Plugin | Description |
|--------|-------------|
| [a11y-audit](plugins/a11y-audit/) | Full accessibility audit with WCAG compliance checking |
| [accessibility-checker](plugins/accessibility-checker/) | Scan for accessibility issues and fix ARIA attributes in web applications |
| [adr-writer](plugins/adr-writer/) | Architecture Decision Records authoring and management |
| [ai-prompt-lab](plugins/ai-prompt-lab/) | Improve and test AI prompts for better Claude Code interactions |
| [analytics-reporter](plugins/analytics-reporter/) | Generate analytics reports and dashboard configurations from project data |
| [android-developer](plugins/android-developer/) | Android and Kotlin development with Jetpack Compose |
| [api-architect](plugins/api-architect/) | API design, documentation, and testing with OpenAPI spec generation |
| [api-benchmarker](plugins/api-benchmarker/) | API endpoint benchmarking and performance reporting |
| [api-reference](plugins/api-reference/) | API reference documentation generation from source code |
| [api-tester](plugins/api-tester/) | Test API endpoints and run load tests against services |
| [aws-helper](plugins/aws-helper/) | AWS service configuration and deployment automation |
| [azure-helper](plugins/azure-helper/) | Azure service configuration and deployment automation |
| [backend-architect](plugins/backend-architect/) | Backend service architecture design with endpoint scaffolding |
| [bug-detective](plugins/bug-detective/) | Debug issues systematically with root cause analysis and execution tracing |
| [bundle-analyzer](plugins/bundle-analyzer/) | Frontend bundle size analysis and tree-shaking optimization |
| [changelog-gen](plugins/changelog-gen/) | Generate changelogs from git history with conventional commit parsing |
| [changelog-writer](plugins/changelog-writer/) | Detailed changelog authoring from git history and PRs |
| [ci-debugger](plugins/ci-debugger/) | Debug CI/CD pipeline failures and fix configurations |
| [code-architect](plugins/code-architect/) | Generate architecture diagrams and technical design documents |
| [code-explainer](plugins/code-explainer/) | Explain complex code and annotate files with inline documentation |
| [code-guardian](plugins/code-guardian/) | Automated code review, security scanning, and quality enforcement |
| [code-review-assistant](plugins/code-review-assistant/) | Automated code review with severity levels and actionable feedback |
| [codebase-documenter](plugins/codebase-documenter/) | Auto-document entire codebase with inline comments and API docs |
| [color-contrast](plugins/color-contrast/) | Color contrast checking and accessible color suggestions |
| [commit-commands](plugins/commit-commands/) | Advanced commit workflows with smart staging and push automation |
| [complexity-reducer](plugins/complexity-reducer/) | Reduce cyclomatic complexity and simplify functions |
| [compliance-checker](plugins/compliance-checker/) | Regulatory compliance verification for GDPR, SOC2, and HIPAA |
| [content-creator](plugins/content-creator/) | Technical content generation for blog posts and social media |
| [context7-docs](plugins/context7-docs/) | Fetch up-to-date library documentation via Context7 for accurate coding |
| [contract-tester](plugins/contract-tester/) | API contract testing with Pact for microserv