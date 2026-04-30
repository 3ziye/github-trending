<div align="center">

[中文](./README.zh-CN.md) · English

# The Overbearing Boss Fell for My ADHD
## Cyberboss: a WeChat bridge for Codex and Claude Code

> "Keep escaping into dopamine if you want. I'll still catch you at the next timestamp."

[![Node >=22](https://img.shields.io/badge/Node-22%2B-3C873A)](./package.json)
[![License: AGPLv3](https://img.shields.io/badge/License-AGPLv3-b31b1b)](./LICENSE)
[![Runtime-Codex%20%7C%20ClaudeCode](https://img.shields.io/badge/Runtime-Codex%20%7C%20ClaudeCode-111827)](#technical-stack)
[![Bridge-Weixin](https://img.shields.io/badge/Bridge-Weixin-07C160)](#technical-stack)
[![Timeline-Enabled](https://img.shields.io/badge/Timeline-Enabled-8b5cf6)](#core-features)

<p>
  <a href="#user-guide">User Guide</a> ·
  <a href="#agent-guide">Agent Guide</a> ·
  <a href="#data-dir">Local Data</a> ·
  <a href="#faq">FAQ</a>
</p>

</div>

<p align="center">
  <img src="./docs/images/IMG_0241.PNG" alt="Cyberboss English demo 1" width="31%" />
  <img src="./docs/images/IMG_0244.PNG" alt="Cyberboss English demo 2" width="31%" />
  <img src="./docs/images/IMG_0245.PNG" alt="Cyberboss English demo 3" width="31%" />
</p>

Cyberboss is not another polite productivity timer. It is not a to-do list with better branding either.

It is an agent bridge that plugs a local coding runtime directly into WeChat and turns it into a time-aware, context-persistent accountability companion. It supports Codex and Claude Code while keeping the same commands and day-to-day behavior. It does not wait for you to "start a session". It watches the flow of your day, notices when you disappear, and decides when to show up again.

## Why Cyberboss?

For people with ADHD, or anyone who needs strong external accountability, most productivity tools fail for the same reason: they assume you still have enough executive function to remember to use them.

Cyberboss starts from a transfer of control.

- No manual start button
  It lives inside the chat interface you actually open every day.
- Inescapable sense of time
  It sees when you replied, when you vanished, and how long a promise stayed unresolved.
- Real external feedback
  If self-discipline is unreliable, hand the supervision layer to an agent that stays online, keeps memory, and can act across time.

<a id="core-features"></a>
## Core Features: fully automated accountability

1. Omniscient Time
Every inbound WeChat message is stamped with local time before it reaches the runtime. The model is not just reading text. It is reading your day as it unfolds.

2. The Ledger of Life
Using those timestamps, Cyberboss reconstructs when events start, when they end, and how long they last, then turns fragmented chat into a structured personal timeline.

3. Stochastic Pulse
At random intervals, the system wakes the agent up and lets it decide what to do next: send a message, stay silent, write in the diary, update the timeline, or use tools.

4. Local Reminder Queue
Reminders are not primarily a user-facing alarm clock. They are how the model leaves instructions for its future self and wakes itself up later.

5. Zero-Token Diary
Daily traces can be written to local files without depending on a cloud note service or burning extra model context every time.

## Timeline also works on its own

If the most interesting part of Cyberboss is the "ledger of life" layer, you can use that separately:

- Project: [WenXiaoWendy/timeline-for-agent](https://github.com/WenXiaoWendy/timeline-for-agent)
- It is an independent project and does not require the WeChat bridge
- You can plug it into your own agent, bot, or automation stack even if you do not use Codex

Cyberboss builds on top of `timeline-for-agent`, then adds WeChat, reminders, diary writing, and random check-ins around it.

<a id="technical-stack"></a>
## Technical Stack

- **Core**
  A pluggable runtime layer for Codex and Claude Code, with the same WeChat command surface and shared-thread workflow.
- **Bridge**
  A WeChat HTTP bridge with long-poll synchronization for inbound messages, outbound replies, files, and status transitions.
- **Task System**
  Local queues for reminders, system triggers, and timeline screenshot jobs.
- **Capability Layer**
  Timeline, diary, random check-ins, file delivery, and related runtime actions.
- **Optional Tooling**
  MCP or other local hardware / software integrations can be added, but they are optional.

## Why It Exists

Cyberboss is built against the myth that productivity begins with self-control.

- Pomodoro assumes you can start on command.
- To-do apps assume you can keep returning.
- Reminder apps assume you will still respect them when they fire.

Cyberboss assumes none of that. It treats the user as someone who may drift, disappear, procrastinate, or lose momentum, then moves the regulatory layer outside the user and into an always-on local agent.

<a id="user-guide"></a>
## User Guide

### Requirements

- Node.js `>= 22`
- `codex` or `claude` installed locally
- Chrome / Ch