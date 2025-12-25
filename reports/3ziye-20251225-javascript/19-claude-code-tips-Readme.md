# 40+ Claude Code Tips: From Basics to Advanced

Here are my tips for getting the most out of Claude Code, including a custom status line script, cutting the system prompt in half, using Gemini CLI as Claude Code's minion, and Claude Code running itself in a container.

📺 [Quick demo](https://www.youtube.com/watch?v=hiISl558JGE) - See some of these tips in action with a multi-Claude workflow and voice input:

[![Demo video thumbnail](assets/demo-thumbnail.png)](https://www.youtube.com/watch?v=hiISl558JGE)

<!-- TOC -->
## Table of Contents

- [Tip 0: Customize your status line](#tip-0-customize-your-status-line)
- [Tip 1: Talk to Claude Code with your voice](#tip-1-talk-to-claude-code-with-your-voice)
- [Tip 2: Break down large problems into smaller ones](#tip-2-break-down-large-problems-into-smaller-ones)
- [Tip 3: Using Git and GitHub CLI like a pro](#tip-3-using-git-and-github-cli-like-a-pro)
- [Tip 4: AI context is like milk; it's best served fresh and condensed!](#tip-4-ai-context-is-like-milk-its-best-served-fresh-and-condensed)
- [Tip 5: Getting output out of your terminal](#tip-5-getting-output-out-of-your-terminal)
- [Tip 6: Set up terminal aliases for quick access](#tip-6-set-up-terminal-aliases-for-quick-access)
- [Tip 7: Proactively compact your context](#tip-7-proactively-compact-your-context)
- [Tip 8: Complete the write-test cycle for autonomous tasks](#tip-8-complete-the-write-test-cycle-for-autonomous-tasks)
- [Tip 9: Cmd+A and Ctrl+A are your friends](#tip-9-cmda-and-ctrla-are-your-friends)
- [Tip 10: Use Gemini CLI as a fallback for blocked sites](#tip-10-use-gemini-cli-as-a-fallback-for-blocked-sites)
- [Tip 11: Invest in your own workflow](#tip-11-invest-in-your-own-workflow)
- [Tip 12: Search through your conversation history](#tip-12-search-through-your-conversation-history)
- [Tip 13: Multitasking with terminal tabs](#tip-13-multitasking-with-terminal-tabs)
- [Tip 14: Slim down the system prompt](#tip-14-slim-down-the-system-prompt)
- [Tip 15: Git worktrees for parallel branch work](#tip-15-git-worktrees-for-parallel-branch-work)
- [Tip 16: Manual exponential backoff for long-running jobs](#tip-16-manual-exponential-backoff-for-long-running-jobs)
- [Tip 17: Claude Code as a writing assistant](#tip-17-claude-code-as-a-writing-assistant)
- [Tip 18: Markdown is the s**t](#tip-18-markdown-is-the-st)
- [Tip 19: Use Notion to preserve links when pasting](#tip-19-use-notion-to-preserve-links-when-pasting)
- [Tip 20: Containers for long-running risky tasks](#tip-20-containers-for-long-running-risky-tasks)
- [Tip 21: The best way to get better at using Claude Code is by using it](#tip-21-the-best-way-to-get-better-at-using-claude-code-is-by-using-it)
- [Tip 22: Clone conversations to branch off](#tip-22-clone-conversations-to-branch-off)
- [Tip 23: Use realpath to get absolute paths](#tip-23-use-realpath-to-get-absolute-paths)
- [Tip 24: Understanding CLAUDE.md vs Skills vs Slash Commands vs Plugins](#tip-24-understanding-claudemd-vs-skills-vs-slash-commands-vs-plugins)
- [Tip 25: Interactive PR reviews](#tip-25-interactive-pr-reviews)
- [Tip 26: Claude Code as a research tool](#tip-26-claude-code-as-a-research-tool)
- [Tip 27: Mastering different ways of verifying its output](#tip-27-mastering-different-ways-of-verifying-its-output)
- [Tip 28: Claude Code as a DevOps engineer](#tip-28-claude-code-as-a-devops-engineer)
- [Tip 29: Keep CLAUDE.md simple and concise](#tip-29-keep-claudemd-simple-and-concise)
- [Tip 30: Claude Code as the universal interface](#tip-30-claude-code-as-the-universal-interface)
- [Tip 31: It's all about choosing the right level of abstraction](#tip-31-its-all-about-choosing-the-right-level-of-abstraction)
- [Tip 32: Audit your approved commands](#tip-32-audit-your-approved-commands)
- [Tip 33: Write lots of tests (and use TDD)](#tip-33-write-lots-of-tests-and-use-tdd)
- [Tip 34: Be braver in the unknown; iterative problem solving](#tip-34-be-braver-in-the-unknown-iterative-problem-solving)
- [Tip 35: Ctrl+B to move commands to the background](#tip-35-ctrlb-to-move-commands-to-the-background)
- [Tip 36: The era of personalized software is here](#tip-36-the-era-of-personalized-software-is-here)
- [Tip 37: Navigating and editing your input box](#tip-37-navigating-and-editing-your-input-box)
- [Tip 38: Spend some time planning, but also prototype quickly](#tip-38-spend-some-time-planning-but-also-prototype-quickly)
- [Tip 39: Simplify overcomplicated code](#tip-39-simplify-overcomplicated-code)
- [Tip 40: Automation of automation](#tip-40-automation-of-automation)
- [Tip 41: Share your knowledge and contribute where you can](#tip-41-share-your-knowledge-and-contribute-where-you-can)
- [Tip 42: Keep learning!](#tip-42-keep-learning)

<!-- /TOC -->

## Tip 0: Customize your status line

You can customize the status line at the bottom of Claude Code to show useful info. I set mine up to show the model, current directory, git branch (if any), uncommitted file count, sync stat