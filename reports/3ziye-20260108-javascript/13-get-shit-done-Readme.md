# Get Shit Done

**A meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.**

![GSD Install](assets/terminal.svg)

<div align="center">
<br>

*"If you know clearly what you want, this WILL build it for you. No bs."*

*"I've done SpecKit, OpenSpec and Taskmaster — this has produced the best results for me."*

*"By far the most powerful addition to my Claude Code. Nothing over-engineered. Literally just gets shit done."*

<br>

**Trusted by engineers at Amazon, Google, Shopify, and Webflow.**

</div>

---

Vibecoding has a bad reputation. You describe what you want, AI generates code, and you get inconsistent garbage that falls apart at scale.

GSD fixes that. It's the context engineering layer that makes Claude Code reliable. Describe your idea, let the system extract everything it needs to know, and let Claude Code get to work.

---

## Who This Is For

People who want to describe what they want and have it built correctly — without pretending they're running a 50-person engineering org.

### Marketplace Installation

Install from the Claude Code marketplace:

```bash
/plugin marketplace add glittercowboy/get-shit-done
/plugin install get-shit-done@get-shit-done
```

### Manual Installation

Clone the repository and tell Claude Code where to find it:

```bash
git clone https://github.com/glittercowboy/get-shit-done.git
claude --plugin-dir ./get-shit-done
```

Useful for development or testing modifications.

---

## Why I Built This

I'm a solo developer. I don't write code — Claude Code does.

Other spec-driven development tools exist; BMAD, Speckit... But they all seem to make things way more complicated than they need to be (sprint ceremonies, story points, stakeholder syncs, retrospectives, Jira workflows) or lack real big picture understanding of what you're building. I'm not a 50-person software company. I don't want to play enterprise theater. I'm just a creative person trying to build great things that work.

So I built GSD. The complexity is in the system, not in your workflow. Behind the scenes: context engineering, XML prompt formatting, subagent orchestration, state management. What you see: a few commands that just work.

The system gives Claude everything it needs to do the work _and_ verify it. I trust the workflow. It just does a good job.

That's what this is. No enterprise roleplay bullshit. Just an incredibly effective system for building cool stuff consistently using Claude Code.

— TÂCHES

---

## Installation

```bash
npx get-shit-done-cc
```

That's it. Works on Mac, Windows, and Linux.

### Non-interactive Install (Docker, CI, Scripts)

```bash
npx get-shit-done-cc --global   # Install to ~/.claude/
npx get-shit-done-cc --local    # Install to ./.claude/
```

Use `--global` (`-g`) or `--local` (`-l`) to skip the interactive prompt.

Verify: `/gsd:help`

### Recommended: Skip Permissions Mode

GSD is designed for frictionless automation. Run Claude Code with:

```bash
claude --dangerously-skip-permissions
```

This is how GSD is intended to be used — stopping to approve `date` and `git commit` 50 times defeats the purpose.

If you prefer not to use that flag, add this to your project's `.claude/settings.json` to auto-approve GSD's commands:

<details>
<summary>Show settings.json permissions</summary>

```json
{
  "permissions": {
    "allow": [
      "Bash(date:*)",
      "Bash(echo:*)",
      "Bash(cat:*)",
      "Bash(ls:*)",
      "Bash(mkdir:*)",
      "Bash(wc:*)",
      "Bash(head:*)",
      "Bash(tail:*)",
      "Bash(sort:*)",
      "Bash(grep:*)",
      "Bash(tr:*)",
      "Bash(git add:*)",
      "Bash(git commit:*)",
      "Bash(git status:*)",
      "Bash(git log:*)",
      "Bash(git diff:*)",
      "Bash(git tag:*)"
    ]
  }
}
```

</details>

---

## How It Works

### 1. Start with an idea

```
/gsd:new-project
```

The system asks questions. Keeps asking until it has everything — your goals, constraints, tech preferences, edge cases. You go back and forth until the idea is fully captured. Creates **PROJECT.md**.

### 2. Create roadmap

```
/gsd:create-roadmap     # Create phases and state tracking
```

Roadmap creation produces:

- **ROADMAP.md** - Phases from start to finish
- **STATE.md** - Living memory that persists across sessions

### 3. Plan and execute phases

```
/gsd:plan-phase 1      # System creates atomic task plans
/gsd:execute-plan      # Subagent implements autonomously
```

Each phase breaks into 2-3 atomic tasks. Each task runs in a fresh subagent context — 200k tokens purely for implementation, zero degradation.

### 4. Ship and iterate

```
/gsd:complete-milestone   # Archive v1, prep for v2
/gsd:add-phase            # Append new work
/gsd:insert-phase 2       # Slip urgent work between phases
```

Ship your MVP in a day. Add features. Insert hotfixes. The system stays modular — you're never stuck.

---

## Existing Projects (Brownfield)

Already have code? Start here instead.

### 1. Map the codebase

```