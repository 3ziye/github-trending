# diff-tour

Walk through a diff the way a senior engineer reads it.

**English** | [日本語](README.ja.md)

[![Release](https://img.shields.io/github/v/release/init-co-jp/diff-tour)](https://github.com/init-co-jp/diff-tour/releases)
[![CI](https://github.com/init-co-jp/diff-tour/actions/workflows/ci.yml/badge.svg)](https://github.com/init-co-jp/diff-tour/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

![tour walking through a change that adds coupons](demo/demo-en.gif)

<sub>A tour of <a href="https://github.com/init-co-jp/diff-tour-example/tree/feature/coupons">a branch that adds coupons</a>: what the change is for, how the usage limit is enforced, a question to think about, and the answer: applying a coupon twice to one order uses it up twice.</sub>

> [!NOTE]
> diff-tour is growing fast. The tour format and the screens may still change from release to release.

## Quick start

You need git and one of [Claude Code](https://claude.com/claude-code), [Codex CLI](https://github.com/openai/codex), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [OpenCode](https://opencode.ai) 2, [Copilot CLI](https://github.com/github/copilot-cli) or [Pi](https://pi.dev), signed in.

```sh
curl -fsSL https://raw.githubusercontent.com/init-co-jp/diff-tour/main/install.sh | sh
cd your-repo
tour
```

Then it goes like this:

1. **Setup** (first time only): choose the display language and the LLM that writes the tour. Both have a recommended choice selected, so press Enter twice.
2. **Pick a change**: the changes you can tour are listed, with your current branch selected. Press Enter.
3. **Writing**: the LLM writes the tour. This takes 2 to 5 minutes.
4. **The tour**: **→** goes forward, **←** goes back, **q** quits.

If `tour` is not found, add the line the install script printed to your shell profile.

To see a finished tour first, with no LLM and no sign-in, play the one from the GIF. It opens at once:

```sh
git clone https://github.com/init-co-jp/diff-tour-example && cd diff-tour-example
curl -fsSLO https://raw.githubusercontent.com/init-co-jp/diff-tour/main/tours/example-coupons.en.json
tour example-coupons.en.json
```

Other ways to install are in [Install](#install), and an example repository to try is in [First run](#first-run).

## What it is

AI can write code that works. It does not teach you *why* the code is written that way, or what a reviewer would worry about.

`tour` turns a git change into a guided tour you step through with two keys, **→** and **←**. The tour shows what a senior engineer looks at when they read the change:

- **How they read it.** What the change is for, where to spend time, and which files to jump to next, including files that did not change.
- **What they ask.** Does it keep the promises the old code kept? What happens when something fails, or runs twice? Can it be rolled out and rolled back safely? Who can call it, and with what input? What happens at 100 times the data? Is the next change easier or harder? Would the tests fail if the code broke?
- **How they judge.** Which findings must be fixed and which are only suggestions or nits, what looks risky but is fine and why, what is done well, and whether the change makes the codebase better overall.
- **Where they stop and say "wait".** These come as questions, so you can predict the answer before you see it.

This view comes from what experienced engineers have written down about reading and reviewing code, collected in [`internal/generate/lessons`](internal/generate/lessons) (in Japanese). The LLM reads it before every tour.

The tour is written by an LLM you already use: Claude Code, Codex CLI, Gemini CLI, OpenCode, Copilot CLI or Pi. `tour` is read-only. It never changes your files or your repository.

## How it works

```text
 your repository                          cache directory (deleted after writing)
 ───────────────                          ──────────────────────────────────────
 git archive <base>  ──────────────────▶  base/          files before the change
 git archive <head>  ──────────────────▶  head/          files after the change
 git diff            ──────────────────▶  change.diff
 git log             ──────────────────▶  commits.txt
 (built into tour)   ──────────────────▶  lessons/       what senior engineers have learned
                                                 │
                                                 ▼
                      Claude Code / Codex / Gemini / OpenCode / Copilot / Pi, started in that directory
                      with read-only permissions. It reads, then writes the
                      tour as JSON.
                                                 │
                                                 ▼
 tour checks every file and line the JSON points to. If something is wrong,
 it asks the LLM to fix only that (up to 2 times). The tour is saved.
                                                 │
                                 