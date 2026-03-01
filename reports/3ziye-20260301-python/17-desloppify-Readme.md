# Desloppify - an agent harness to make your codebase 🤌

[![PyPI version](https://img.shields.io/pypi/v/desloppify)](https://pypi.org/project/desloppify/) ![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)

Desloppify gives your AI coding agent the tools to identify, understand, and systematically improve codebase quality. It combines mechanical detection (dead code, duplication, complexity) with subjective LLM review (naming, abstractions, module boundaries), then works through a prioritized fix loop. State persists across scans so it chips away over multiple sessions, and the scoring is designed to resist gaming.

<img src="assets/explained.png" width="100%">

The score gives your agent a north-star, and the tooling helps it plan, execute, and resolve issues until it hits your target — with a lot of tricks to keep it on track. A score above 98 should correlate with a codebase a seasoned engineer would call beautiful.

That score generates a scorecard badge for your GitHub profile or README:

<img src="assets/scorecard.png" width="100%">

Currently supports 28 languages — full plugin depth for TypeScript, Python, C#, Dart, GDScript, and Go; generic linter + tree-sitter support for Rust, Ruby, Java, Kotlin, and 17 more.

## For your agent's consideration...

Paste this prompt into your agent:

```
I want you to improve the quality of this codebase. To do this, install and run desloppify.
Run ALL of the following (requires Python 3.11+):

pip install --upgrade "desloppify[full]"
desloppify update-skill claude    # IMPORTANT — installs the workflow guide. Pick yours: claude, cursor, codex, copilot, windsurf, gemini
desloppify scan --path .
desloppify next

--path is the directory to scan (use "." for the whole project, or "src/" etc).

Your goal is to get the strict score that Desloppify produces as high as possible. Don't be lazy. Fix things properly
and fix things deep. Large refactors are fine if that's what it takes but also small fixes are great. The scoring is designed
to resist gaming, so the only way to improve it is to actually make the code better. Don't cheat.

Follow `next` — it tells you exactly what to fix, which file, and the resolve command to run
when done. Fix the issue, resolve it, run `next` again. Keep going until done.
Use `plan` to reorder priorities or cluster related issues.
You can scan to refresh things. The scan output includes agent instructions — follow them, don't augment with your own analysis but follow its plan.
```

## From Vibe Coding to Vibe Engineering

Vibe coding gets things built fast. But the codebases it produces tend to rot in ways that are hard to see and harder to fix — not just the mechanical stuff like dead imports, but the structural kind. Abstractions that made sense at first stop making sense. Naming drifts. Error handling is done three different ways. The codebase works, but working in it gets worse over time.

LLMs are actually good at spotting this now, if you ask them the right questions. That's the core bet here — that an agent with the right framework can hold a codebase to a real standard, the kind that used to require a senior engineer paying close attention over months.

So we're trying to define what "good" looks like as a score that's actually worth optimizing. Not a lint score you game to 100 by suppressing warnings. Something where improving the number means the codebase genuinely got better. That's hard, and we're not done, but the anti-gaming stuff matters to us a lot — it's the difference between a useful signal and a vanity metric.

The hope is that anyone can use this to build something a seasoned engineer would look at and respect. That's the bar we're aiming for.

If you'd like to join a community of vibe engineers who want to build beautiful things, [come hang out](https://discord.gg/aZdzbZrHaY).

<img src="assets/engineering.png" width="100%">

---

<details>
<summary><strong>Stuff you probably won't need to know</strong></summary>

#### Commands

| Command | Description |
|---------|-------------|
| `scan [--reset-subjective]` | Run all detectors, update state (optional: reset subjective baseline to 0 first) |
| `status` | Score + per-tier progress |
| `show <pattern>` | Findings by file, directory, detector, or ID |
| `next [--tier N] [--explain]` | Highest-priority open finding (--explain: with score context) |
| `resolve <status> <patterns>` | Mark open / fixed / wontfix / false_positive |
| `fix <fixer> [--dry-run]` | Auto-fix mechanical issues |
| `review --prepare` | Generate subjective review packet (`query.json`) |
| `review --run-batches --runner codex --parallel` | Run blind subjective batch assessments, merge/import, optionally `--scan-after-import` |
| `review --import <file> [--allow-partial]` | Import subjective review findings (fails closed on invalid findings by default) |
| `review --external-start --external-runner claude` | Start Claude cloud blind-review session (creates session/token/template) |
| `re