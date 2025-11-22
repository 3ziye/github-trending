# Claude Code Infrastructure Showcase

**A curated reference library of production-tested Claude Code infrastructure.**

Born from 6 months of real-world use managing a complex TypeScript microservices project, this showcase provides the patterns and systems that solved the "skills don't activate automatically" problem and scaled Claude Code for enterprise development.

> **This is NOT a working application** - it's a reference library. Copy what you need into your own projects.

---

## What's Inside

**Production-tested infrastructure for:**
- ✅ **Auto-activating skills** via hooks
- ✅ **Modular skill pattern** (500-line rule with progressive disclosure)
- ✅ **Specialized agents** for complex tasks
- ✅ **Dev docs system** that survives context resets
- ✅ **Comprehensive examples** using generic blog domain

**Time investment to build:** 6 months of iteration
**Time to integrate into your project:** 15-30 minutes

---

## Quick Start - Pick Your Path

### 🤖 Using Claude Code to Integrate?

**Claude:** Read [`CLAUDE_INTEGRATION_GUIDE.md`](CLAUDE_INTEGRATION_GUIDE.md) for step-by-step integration instructions tailored for AI-assisted setup.

### 🎯 I want skill auto-activation

**The breakthrough feature:** Skills that actually activate when you need them.

**What you need:**
1. The skill-activation hooks (2 files)
2. A skill or two relevant to your work
3. 15 minutes

**👉 [Setup Guide: .claude/hooks/README.md](.claude/hooks/README.md)**

### 📚 I want to add ONE skill

Browse the [skills catalog](.claude/skills/) and copy what you need.

**Available:**
- **backend-dev-guidelines** - Node.js/Express/TypeScript patterns
- **frontend-dev-guidelines** - React/TypeScript/MUI v7 patterns
- **skill-developer** - Meta-skill for creating skills
- **route-tester** - Test authenticated API routes
- **error-tracking** - Sentry integration patterns

**👉 [Skills Guide: .claude/skills/README.md](.claude/skills/README.md)**

### 🤖 I want specialized agents

10 production-tested agents for complex tasks:
- Code architecture review
- Refactoring assistance
- Documentation generation
- Error debugging
- And more...

**👉 [Agents Guide: .claude/agents/README.md](.claude/agents/README.md)**

---

## What Makes This Different?

### The Auto-Activation Breakthrough

**Problem:** Claude Code skills just sit there. You have to remember to use them.

**Solution:** UserPromptSubmit hook that:
- Analyzes your prompts
- Checks file context
- Automatically suggests relevant skills
- Works via `skill-rules.json` configuration

**Result:** Skills activate when you need them, not when you remember them.

### Production-Tested Patterns

These aren't theoretical examples - they're extracted from:
- ✅ 6 microservices in production
- ✅ 50,000+ lines of TypeScript
- ✅ React frontend with complex data grids
- ✅ Sophisticated workflow engine
- ✅ 6 months of daily Claude Code use

The patterns work because they solved real problems.

### Modular Skills (500-Line Rule)

Large skills hit context limits. The solution:

```
skill-name/
  SKILL.md                  # <500 lines, high-level guide
  resources/
    topic-1.md              # <500 lines each
    topic-2.md
    topic-3.md
```

**Progressive disclosure:** Claude loads main skill first, loads resources only when needed.

---

## Repository Structure

```
.claude/
├── skills/                 # 5 production skills
│   ├── backend-dev-guidelines/  (12 resource files)
│   ├── frontend-dev-guidelines/ (11 resource files)
│   ├── skill-developer/         (7 resource files)
│   ├── route-tester/
│   ├── error-tracking/
│   └── skill-rules.json    # Skill activation configuration
├── hooks/                  # 6 hooks for automation
│   ├── skill-activation-prompt.*  (ESSENTIAL)
│   ├── post-tool-use-tracker.sh   (ESSENTIAL)
│   ├── tsc-check.sh        (optional, needs customization)
│   └── trigger-build-resolver.sh  (optional)
├── agents/                 # 10 specialized agents
│   ├── code-architecture-reviewer.md
│   ├── refactor-planner.md
│   ├── frontend-error-fixer.md
│   └── ... 7 more
└── commands/               # 3 slash commands
    ├── dev-docs.md
    └── ...

dev/
└── active/                 # Dev docs pattern examples
    └── public-infrastructure-repo/
```

---

## Component Catalog

### 🎨 Skills (5)

| Skill | Lines | Purpose | Best For |
|-------|-------|---------|----------|
| [**skill-developer**](.claude/skills/skill-developer/) | 426 | Creating and managing skills | Meta-development |
| [**backend-dev-guidelines**](.claude/skills/backend-dev-guidelines/) | 304 | Express/Prisma/Sentry patterns | Backend APIs |
| [**frontend-dev-guidelines**](.claude/skills/frontend-dev-guidelines/) | 398 | React/MUI v7/TypeScript | React frontends |
| [**route-tester**](.claude/skills/route-tester/) | 389 | Testing authenticated routes | API testing |
| [**error-tracking**](.claude/skills/error-tracking/) | ~250 | Sentry integration | Error monitoring |

**All skills follow the modular pattern** - main