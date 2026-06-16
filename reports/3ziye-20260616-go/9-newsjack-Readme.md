# Newsjack.sh

**The open-source skills that turn your agent into a full PR team.**

Install once. Your agent — Claude Code, Codex, Hermes, OpenClaw — becomes a PR team.

```bash
curl -fsSL newsjack.sh | bash
```

**Are you an agent?** Check out **[Getting started](docs/getting-started.md)**

**Are you a human?** 📋 Copy this prompt to any AI:

```text
help me setup https://newsjack.sh
```

Jump to **[platform-specific setup](#install)** below for per platform breakdown.

---

## What your agent can do once newsjack is installed

Three problems, separate lanes.

### 🛰️ Detect — surface what matters in your space

- 📡 **Monitor your industry** — find newsjacking opportunities: fresh stories you have the standing to jump on before the wave breaks ([see a sample run](docs/example-run.md))
- 🗞️ **Track your coverage** — Google Alerts-style keyword tracking with LLM filtering for real features
- 🔭 **Track competitors** — when they launch, raise, or stumble, you know
- 🔍 **Verify the story is still fresh** — who broke it, who owns it, what oxygen's left

### 🚀 Act — turn signal into output

- 🎯 **Generate story angles** — turn one update into hooks framed for different beats
- 🤝 **Fit-check a journalist** — will *this* reporter actually care, or are you spamming?
- 🎙️ **Respond to source queries** — triage inbound HARO-style requests, draft only the real fits
- 🥊 **Roast your pitch** — honest critique against the rubric editors actually use
- ✅ **Fact-check before you send** — extract claims, verify each, flag the shaky ones
- 🗣️ **Keep drafts in your voice** — fingerprint your real writing, kill the AI tells
- 📋 **Build a fit-checked media list** — targeted reporters, not scraped contact dumps

### 🧭 Strategize — figure out what your story even is

- 🗺️ **Get a PR strategy** — opinionated walkthrough if you're not PR-fluent yet: audience first, positioning second, news pegs third, drumbeat over big-bang
- 📊 **Score newsworthiness** — cold read on whether it clears the bar before you act

---

## Who this is for

- **Founders** doing their own PR because the agency quote was insane
- **PR agencies** running more accounts than humans can babysit
- **Marketers** at small companies who need leverage, not headcount
- **Anyone** whose agent is already running their day-to-day — and should be better at it

---

## Install

Newsjack is a set of **open skills** — plain-Markdown instructions your agent
reads — plus a small open-source CLI. Most skills run anywhere your agent runs.
A few reach for a live news index, journalist enrichment,
or locally-saved monitoring state — those work best in a local agent.

### What runs where

| Skill | [Claude.ai](https://claude.ai) | [ChatGPT](https://chatgpt.com) | [Cowork](https://claude.com/product/cowork) | [Claude Code](https://claude.com/claude-code) | [Codex](https://openai.com/codex) | [Hermes](https://hermes-agent.nousresearch.com) | [OpenClaw](https://openclaw.ai) | [Medialyst](https://medialyst.ai) |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Strategize** | | | | | | | | |
| pr-strategist | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| newsworthiness-check | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Act** | | | | | | | | |
| angle-generator | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| headline-generator | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| meanest-editor | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| crisis-holding | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| reactive-comment | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| fact-check | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| journalist-fit-check | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| voice-extractor | ⚠️ | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| find-journalists | 🔧 | ⚠️ | 🔧 | 🔧 | 🔧 | 🔧 | 🔧 | ✅ |
| **Detect** | | | | | | | | |
| news-search | ✅ | ⚠️ | 🔧 | 🔧 | 🔧 | 🔧 | 🔧 | ✅ |
| story-origin-check | 🔧 | ⚠️ | 🔧 | 🔧 | 🔧 | 🔧 | 🔧 | ✅ |
| relevance-coarse-filter | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| newsjack-triage | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| newsjack-detector | ⚠️ | ⚠️ | ⚠️ | 🔧 | 🔧 | 🔧 | 🔧 | 🔜 |
| newsjack-monitor-setup | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | 🔜 |
| coverage-tracker | ⚠️ | ⚠️ | ⚠️ | ✅ | ✅ | ✅ | ✅ | 🔜 |
| coverage-tracker-setup | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | 🔜 |


Legend:

- **✅ Runs out of the box** — no setup; works anywhere your agent does.
- **🔧 May need an external connection** — works on its own, but does its best work with an external data source connected (e.g. the X API or the Medialyst API).
- **⚠️ Limited Mode** — runs in a chat app, but as a best-effort, one-shot pass with nothing saved between sessions: no stored voice fingerprint, no scheduled monitoring, no repeat-suppression. Connect a local agent for the saved, scheduled version.
- **🔜 Coming soon** — not available here yet.
- **❌ Not supported** — the two setup skills (`newsjack-monitor-setup`, `coverage-tracker-setup`) only save a profile or config and schedule it, so they need a local agent.

**Set up your agent:**

- **[Local agents](#local-agents-claude-code-codex-hermes-openclaw)** 