<div>
<div align="right">
<a href="https://piebald.ai"><img width="200" top="20" align="right" src="https://github.com/Piebald-AI/.github/raw/main/Wordmark.svg"></a>
</div>

<div align="left">

### Announcement: Piebald is released!
We've released **Piebald**, the ultimate agentic AI developer experience. \
Download it and try it out for free!  **https://piebald.ai/**

<sub>[Scroll down for Claude Code's system prompts.](https://github.com/Piebald-AI/claude-code-system-prompts#claude-code-system-prompts) :point_down:</sub>

</div>
</div>

<div align="left">
<a href="https://piebald.ai">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/79c18689-e2f0-4008-a13f-61c80756286a">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/25cb5df8-cf15-4cae-9c1e-e88645f06ee1">
  <img alt="hero" width="600" src="https://github.com/user-attachments/assets/25cb5df8-cf15-4cae-9c1e-e88645f06ee1">
</picture>
</a>
</div>

# Claude Code System Prompts

This repository contains an up-to-date list of all Claude Code's various system prompts and their associated token counts as of **[Claude Code v2.0.71](https://www.npmjs.com/package/@anthropic-ai/claude-code/v/2.0.71) (December 16th, 2025).**  It also contains a [**CHANGELOG.md**](./CHANGELOG.md) for the system prompts across 52 versions since v2.0.14.  From the team behind [<img src="https://github.com/Piebald-AI/piebald/raw/main/assets/logo.svg" width="15"> **Piebald.**](https://piebald.ai/)

Why multiple "system prompts?"

**Claude Code doesn't just have one single string for its system prompt.**

Instead, there are:
- Large portions conditionally added depending on the environment and various configs.
- Descriptions for builtin tools like `Write`, `Bash`, and `TodoWrite`, and some are fairly large.
- Separate system prompts for builtin agents like Explore and Plan.
- Numerous AI-powered utility functions, such as conversation compaction, `CLAUDE.md` generation, session title generation, etc. featuring their own systems prompts.

The result&mdash;40+ strings that are constantly changing and moving within a very large minified JS file.

> [!TIP]
> Want to **modify a particular piece of the system prompt** in your own Claude Code installation?  **Use [tweakcc](https://github.com/Piebald-AI/tweakcc).**  It&mdash;
> - lets you customize the the individual pieces of the system prompt as markdown files, and then
> - patches your npm-based or native (binary) Claude Code installation with them, and also
> - provides diffing and conflict management for when both you and Anthropic have conflicting modifications to the same prompt file.

## Prompts

Note that some prompts contain interpolated bits such as builtin tool name references, lists of available sub agents, and various other context-specific variables, so the actual counts in a particular Claude Code session will differ slightly&mdash;likely not beyond ±20 tokens, however.

### Agent Prompts

Sub-agents and utilities.

#### Sub-agents

- [Agent Prompt: Explore](./system-prompts/agent-prompt-explore.md) (**516** tks) - System prompt for the Explore subagent.
- [Agent Prompt: Plan mode (enhanced)](./system-prompts/agent-prompt-plan-mode-enhanced.md) (**633** tks) - Enhanced prompt for the Plan subagent.
- [Agent Prompt: Task tool (extra notes)](./system-prompts/agent-prompt-task-tool-extra-notes.md) (**129** tks) - Additional notes for using the Task tool effectively.
- [Agent Prompt: Task tool](./system-prompts/agent-prompt-task-tool.md) (**294** tks) - System prompt given to the subagent spawned via the Task tool.

### Creation Assistants

- [Agent Prompt: Agent creation architect](./system-prompts/agent-prompt-agent-creation-architect.md) (**1111** tks) - System prompt for creating custom AI agents with detailed specifications.
- [Agent Prompt: CLAUDE.md creation](./system-prompts/agent-prompt-claudemd-creation.md) (**384** tks) - System prompt for analyzing codebases and creating CLAUDE.md documentation files.
- [Agent Prompt: Status line setup](./system-prompts/agent-prompt-status-line-setup.md) (**1310** tks) - System prompt for the statusline-setup agent that configures status line display.

### Slash commands

- [Agent Prompt: /pr-comments slash command](./system-prompts/agent-prompt-pr-comments-slash-command.md) (**402** tks) - System prompt for fetching and displaying GitHub PR comments.
- [Agent Prompt: /review-pr slash command](./system-prompts/agent-prompt-review-pr-slash-command.md) (**243** tks) - System prompt for reviewing GitHub pull requests with code analysis.
- [Agent Prompt: /security-review slash](./system-prompts/agent-prompt-security-review-slash.md) (**2610** tks) - Comprehensive security review prompt for analyzing code changes with focus on exploitable vulnerabilities.

### Utilities

- [Agent Prompt: Agent Hook](./system-prompts/agent-prompt-agent-hook.md) (**133** tks) - Prompt for an 'agent hook'.
-