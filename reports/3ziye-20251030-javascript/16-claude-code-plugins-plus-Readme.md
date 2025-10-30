# Claude Code Plugins

[![Version](https://img.shields.io/badge/version-1.2.5-brightgreen)](CHANGELOG.md)
[![Plugins](https://img.shields.io/badge/plugins-236-blue)](https://github.com/jeremylongshore/claude-code-plugins)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-168%20plugins-orange?logo=sparkles)](CHANGELOG.md#123---2025-10-23)
[![Spec Compliant](https://img.shields.io/badge/Anthropic%20Spec-v1.0%20Compliant-success?logo=checkmarx)](https://github.com/anthropics/skills/blob/main/agent_skills_spec.md)
[![NEW](https://img.shields.io/badge/NEW-Agent%20Context%20Manager-blueviolet?logo=sparkles)](plugins/productivity/agent-context-manager/)
[![GitHub Stars](https://img.shields.io/github/stars/jeremylongshore/claude-code-plugins?style=social)](https://github.com/jeremylongshore/claude-code-plugins)

**236 production-ready Claude Code plugins for automation, development, and AI workflows.**
🎯 **NEW in v1.2.4:** **Excel Analyst Pro** - Professional financial modeling toolkit with auto-invoked Skills and Excel MCP integration!

**Latest:** [v1.2.4 Release](https://github.com/jeremylongshore/claude-code-plugins/releases/tag/v1.2.4) - Excel Analyst Pro plugin for DCF models, LBO analysis, and financial modeling

```bash
/plugin marketplace add jeremylongshore/claude-code-plugins
/plugin install devops-automation-pack@claude-code-plugins-plus
```

💖 **[Sponsor this project](docs/sponsor/)** - Get early access, premium plugins, and priority support

---

## 🎯 Featured: Excel Analyst Pro

**Professional Financial Modeling with Auto-Invoked Skills**

The new [Excel Analyst Pro](plugins/business-tools/excel-analyst-pro/) plugin brings investment banking-grade financial modeling to Claude Code with automatic Skills activation and Excel MCP integration.

```bash
# Install the plugin
/plugin install excel-analyst-pro@claude-code-plugins-plus

# Build a DCF model with natural language
"Build a 5-year DCF model for a SaaS company with 30% revenue growth"

# Create an LBO analysis
/build-lbo

# Analyze budget variance
/analyze-variance
```

**Four Auto-Invoked Skills:**
- **DCF Modeler**: Build discounted cash flow valuation models
- **LBO Modeler**: Create leveraged buyout analysis with debt schedules
- **Variance Analyzer**: Generate executive variance reports
- **Pivot Wizard**: Create pivot tables with natural language

**Why This Matters:**
- Build complex financial models without remembering formulas
- Investment banking-grade templates and best practices
- Local Excel processing - no cloud upload required
- Perfect timing with Anthropic's Claude for Excel announcement
- Auto-invoked Skills activate automatically when needed
- Comprehensive documentation with real-world examples

[Read the full documentation →](plugins/business-tools/excel-analyst-pro/README.md)

---

## 🆕 What's New in v1.2.3

### 🎯 Agent Context Manager Plugin

**NEW**: Automatic AGENTS.md detection and loading alongside CLAUDE.md

- **Plugin**: [agent-context-manager](plugins/productivity/agent-context-manager/)
- **Category**: Productivity
- **Agent Skills**: 1 (agent-context-loader with 200+ line documentation)
- **Slash Commands**: 1 (/sync-agent-context)
- **Hooks**: 2 (onSessionStart, onDirectoryChange)

**Features**:
- Proactive auto-loading when AGENTS.md is detected
- Directory change hooks with formatted visual feedback
- Manual sync command for permanent CLAUDE.md merge
- Three-layer redundancy system
- Comprehensive documentation (400+ lines)
- 100% Anthropic Agent Skills Spec v1.0 compliant
- Exceeds Anthropic standards for documentation depth

**Updates**:
- Plugin count: 236 (with 3 new Vertex AI and Google Cloud plugins)
- Agent Skills count: 168

[Install now →](plugins/productivity/agent-context-manager/)

---

## What's New in v1.2.1

### ✅ Anthropic Official Spec v1.0 Compliance

**All 167 Agent Skills now comply with [Anthropic's official Agent Skills Spec v1.0](https://github.com/anthropics/skills/blob/main/agent_skills_spec.md)** released October 16, 2025.

**What Changed:**
- **Structure migration**: Moved from `skills/skill-adapter/` to `skills/{descriptive-name}/` per Anthropic specification
- **Name format updated**: Title Case → hyphen-case (e.g., "Database Backup Automator" → "database-backup-automator")
- **100% spec compliant**: All SKILL.md files follow official format requirements
- **Forward compatible**: Ensures compatibility with future Claude Code releases
- **No breaking changes**: Skills continue to work exactly as before

**Quality Assessment:**
Our comprehensive internal analysis shows our 167 skills **exceed Anthropic's 17 official examples** in documentation depth, trigger phrase specificity, and workflow detail.

**Automated with:**
- `scripts/migrate-skills.py` - Structure migration tool
- `scripts/fix-skill-names.py` - Batch conversion tool with validation
- 167 skills migrated and validated, 100% success rate

---

## What's New in v1.2.0

### 🎯 Agent Skills Quality Enhancement

**159 h