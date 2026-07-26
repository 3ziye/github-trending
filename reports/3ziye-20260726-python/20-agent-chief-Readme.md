<div align="center">

<img src="docs/assets/logo.png" alt="Chief" width="640"/>

</div>

https://github.com/user-attachments/assets/1177a237-3f0f-4512-baef-dcc9f2c75c6d

<div align="center">

**Your agents don't need more power. They need a chief of staff.**

[![CI](https://github.com/SmileLikeYe/agent-chief/actions/workflows/ci.yml/badge.svg)](https://github.com/SmileLikeYe/agent-chief/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/SmileLikeYe/agent-chief?color=6366f1)](https://github.com/SmileLikeYe/agent-chief/releases)
[![PyPI](https://img.shields.io/pypi/v/agent-chief)](https://pypi.org/project/agent-chief/)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue)](pyproject.toml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Local First](https://img.shields.io/badge/local--first-no%20cloud%2C%20no%20telemetry-8b5cf6)](#privacy)

[Quickstart](#-60-second-quickstart) · [How it works](#-how-it-decides) ·
[Evaluated, not asserted](#-evaluated-not-asserted) ·
[Connect your agent](#-connect-your-agent) · [Docs](docs/) ·
[简体中文](README.zh-CN.md)

</div>

---

<!-- metrics:start -->
**24 events in → 1 interruption** (96% intercepted: 14 blocked outright, the rest batched, dispatched, or remembered)
· only **75% of events ever reach the LLM** — the noisiest 25% dies on hard rules in microseconds, for free
· stable-prefix prompts: **70% of judge input tokens cache-hit** (system + context blocks)
· projected judgment cost **$0.104 per 1,000 events** (DeepSeek list prices, cache-aware)

*(every number regenerates from the deterministic demo replay: `make readme-metrics`)*
<!-- metrics:end -->

Chief sits between you and everything that wants your attention — agents,
heartbeats, CI, RSS, watchers. Everything flows into it; it thinks for itself;
then it does exactly one of three things:

1. 🔔 **Interrupt** you — only when worth it, at the right moment, *arriving with a plan*.
2. 🤖 **Dispatch** work to your agents — and verify the result before reporting ("done" is a claim, not a proof).
3. 📚 **Curate** into memory — facts and intents not worth mentioning now, waiting to be connected later.

<div align="center">

![demo](docs/assets/demo.gif)

*A day of an engineer's life: 24 events in → 14 blocked · 6 batched · 3 handled · **interrupted exactly once**.*

</div>

## ✨ Highlights

| | |
|---|---|
| 🧠 **Three-stage worthiness engine** | Hard rules (µs) → similarity classifier (ms) → LLM judge (only when needed). Cheap first, smart last. |
| 🎭 **Scene-aware timing** | Sleeping / deep work / meeting / commute — per-scene interrupt thresholds. The *same* event rings at your desk and waits in a digest at 2 AM. |
| 🕶️ **Shadow mode** | For its first 7 days Chief never actually interrupts — it shows you what it *would* have done, and earns the right to ring. |
| 📝 **Explainable, editable policy** | Everything it learns distills nightly into a human-readable `POLICY.md`. Your edits win, effective immediately. |
| ✅ **Verified dispatch** | Agents report "done"; Chief checks. Acceptance command or LLM second opinion — fails closed. |
| 🔌 **Protocol, not pipes** | In: one `POST /v1/events` (or MCP `propose`, or `chief push "…"`) connects anything in minutes — message your Telegram bot and the verdict comes back to your phone. Out: one signed webhook makes any HTTP receiver a delivery channel. |
| 🔒 **Local-first** | One SQLite file + markdown under `~/.chief`. No hosted service or telemetry; the local console stays on `127.0.0.1`. |
| 🔬 **Evaluated, not asserted** | 418 offline tests, a 200-case golden set, a **100-user** learning benchmark, per-decision USD cost. Every claim below ships with a command that proves it. |

## ⚡ 60-second quickstart

```bash
uvx agent-chief demo        # zero keys, zero config, fully offline
```

Prefer pip? `pip install agent-chief` installs the same `chief` command.

You'll watch a day of an engineer's life replay: 24 events in → 14 blocked ·
6 batched · 3 handled (all verified) · **interrupted exactly once**.

Ready for real sources?

```bash
uv tool install agent-chief # install the persistent `chief` command
chief init                  # 60s wizard, every question skippable
chief run                   # resident brain + local console
```

## 🔕 Kill the "all clear" reports

If you run heartbeat agents, you know the ritual: *"All clear, nothing to
report."* Every few hours. Forever. Each one costs a glance, and the glances
add up until you stop reading — including the one that mattered.

Chief drops zero-information reports on the floor (regex **and** embedding
similarity against a canned empty-report set, both required — a security scan
that *mentions* "all clear" still gets through). The demo opens and closes with
this, because it's the single most requested feature a