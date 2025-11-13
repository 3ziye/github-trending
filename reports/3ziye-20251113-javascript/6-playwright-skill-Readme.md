# Playwright Skill for Claude Code

**General-purpose browser automation as a Claude Skill**

A [Claude Skill](https://www.anthropic.com/news/skills) that enables Claude to write and execute any Playwright automation on-the-fly - from simple page tests to complex multi-step flows. Packaged as a [Claude Code Plugin](https://docs.claude.com/en/docs/claude-code/plugins) for easy installation and distribution.

Claude autonomously decides when to use this skill based on your browser automation needs, loading only the minimal information required for your specific task.

Made using Claude Code.

## Features

- **Any Automation Task** - Claude writes custom code for your specific request, not limited to pre-built scripts
- **Visible Browser by Default** - See automation in real-time with `headless: false`
- **Zero Module Resolution Errors** - Universal executor ensures proper module access
- **Progressive Disclosure** - Concise SKILL.md with full API reference loaded only when needed
- **Safe Cleanup** - Smart temp file management without race conditions
- **Comprehensive Helpers** - Optional utility functions for common tasks

## Installation

This repository is structured as a [Claude Code Plugin](https://docs.claude.com/en/docs/claude-code/plugins) containing a skill. You can install it as either a **plugin** (recommended) or extract it as a **standalone skill**.

### Understanding the Structure

This repository uses the plugin format with a nested structure:
```
playwright-skill/              # Plugin root
├── .claude-plugin/           # Plugin metadata
└── skills/
    └── playwright-skill/     # The actual skill
        └── SKILL.md
```

Claude Code expects skills to be directly in folders under `.claude/skills/`, so manual installation requires extracting the nested skill folder.

---

### Option 1: Plugin Installation (Recommended)

Install via Claude Code's plugin system for automatic updates and team distribution:

```bash
# Add this repository as a marketplace
/plugin marketplace add lackeyjb/playwright-skill

# Install the plugin
/plugin install playwright-skill@playwright-skill

# Navigate to the skill directory and run setup
cd ~/.claude/plugins/marketplaces/playwright-skill/skills/playwright-skill
npm run setup
```

Verify installation by running `/help` to confirm the skill is available.

---

### Option 2: Standalone Skill Installation

To install as a standalone skill (without the plugin system), extract only the skill folder:

**Global Installation (Available Everywhere):**
```bash
# Clone to a temporary location
git clone https://github.com/lackeyjb/playwright-skill.git /tmp/playwright-skill-temp

# Copy only the skill folder to your global skills directory
mkdir -p ~/.claude/skills
cp -r /tmp/playwright-skill-temp/skills/playwright-skill ~/.claude/skills/

# Navigate to the skill and run setup
cd ~/.claude/skills/playwright-skill
npm run setup

# Clean up temporary files
rm -rf /tmp/playwright-skill-temp
```

**Project-Specific Installation:**
```bash
# Clone to a temporary location
git clone https://github.com/lackeyjb/playwright-skill.git /tmp/playwright-skill-temp

# Copy only the skill folder to your project
mkdir -p .claude/skills
cp -r /tmp/playwright-skill-temp/skills/playwright-skill .claude/skills/

# Navigate to the skill and run setup
cd .claude/skills/playwright-skill
npm run setup

# Clean up temporary files
rm -rf /tmp/playwright-skill-temp
```

**Why this structure?** The plugin format requires the `skills/` directory for organizing multiple skills within a plugin. When installing as a standalone skill, you only need the inner `skills/playwright-skill/` folder contents.

---

### Option 3: Download Release

1. Download and extract the latest release from [GitHub Releases](https://github.com/lackeyjb/playwright-skill/releases)
2. Copy only the `skills/playwright-skill/` folder to:
   - Global: `~/.claude/skills/playwright-skill`
   - Project: `/path/to/your/project/.claude/skills/playwright-skill`
3. Navigate to the skill directory and run setup:
   ```bash
   cd ~/.claude/skills/playwright-skill  # or your project path
   npm run setup
   ```

---

### Verify Installation

Run `/help` to confirm the skill is loaded, then ask Claude to perform a simple browser task like "Test if google.com loads".

## Quick Start

After installation, simply ask Claude to test or automate any browser task. Claude will write custom Playwright code, execute it, and return results with screenshots and console output.

## Usage Examples

### Test Any Page
```
"Test the homepage"
"Check if the contact form works"
"Verify the signup flow"
```

### Visual Testing
```
"Take screenshots of the dashboard in mobile and desktop"
"Test responsive design across different viewports"
```

### Interaction Testing
```
"Fill out the registration form and submit it"
"Click through the main navigation"
"Test the search functionality"
```

### Validation
```
"Check for broken links"
"Verify all images load"
"Test form 