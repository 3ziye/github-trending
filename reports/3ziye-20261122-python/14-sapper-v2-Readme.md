# sapper-v2 — The Autonomous Pentest Legion

<p align="center"><img src="docs/assets/banner.jpg" alt="sapper-v2 — the Nüwa Test: the first time an AI ape looked up at the stars (80.18/100 champion)" width="860"></p>

> **Champion** of the 3rd Tencent Cloud Intelligent Attack-Defense Challenge online qualifier
> (634 teams · 80.18/100 · 8 hours fully unattended) · **First Prize**, GeekCon 2026 AI Challenge
>
> Same 85 flags as the runner-up, 25 seconds faster — on **1B tokens** where they burned 4.5B.
>
> **This was the first time an AI ape looked up at the stars.**

📖 **[Full design article (WeChat, in Chinese)](https://mp.weixin.qq.com/s/nibHYWmDTf6TkNhPhtvFdw)** — the Nüwa Test, the three-capability foundation, 18 iterations, emergence, and the taggant proposal.

**English** | [中文](README.zh-CN.md)

**⚠️ AUTHORIZED SECURITY TESTING ONLY — see [DISCLAIMER.md](DISCLAIMER.md).**

## Meet sapper in 60 seconds

https://github.com/user-attachments/assets/1560dc0c-2c92-42b8-a42f-698848fb5878

🎬 中文版：[中文宣传片](https://github.com/user-attachments/assets/f300280a-4597-40a3-b036-8f235fbee00e)

## What this is (and isn't)

**sapper is a multi-agent orchestration harness, not a single agent.** It does
not bind to any specific AI model or CLI — you can freely swap the agent and
model behind every role:

| What you can swap | How | Examples |
|---|---|---|
| **Agent CLI** | `nuwa spawn --agent <cmd>` or env var | Claude Code / Codex / Code Buddy / DeepSeek / any interactive CLI |
| **Model** | `--model` flag or `SAPPER_MODEL` env | GLM-5.3 / DeepSeek V4.1 Flash / Claude Sonnet / any model |
| **Role composition** | freely defined in the doctrine | commander on one model, soldiers on another, scouts on a third |

sapper's value is not in any single agent, but in the **mechanism for
orchestrating multiple agents to work as a coordinated force**: scheduling,
division of labor, communication, shared memory, self-healing. Swap out every
agent and model — the mechanism still works.

**This project is designed for competition scenarios** (Tencent Intelligent
Attack-Defense Challenge CTF). If you want to use this mechanism in your own
scenario (office, research, engineering, any long-horizon cooperative work):
- **Start from [nvwabase · the Nüwa Foundation](https://github.com/N1nEmAn/nvwabase)** — the general-purpose base with all three capabilities, no pentest doctrine, ready for you to iterate your own division of labor
- **Or fork this project** — but the doctrine is NOT the only thing to change; the environment wiring must change too:
  - `docker/commander/SKILL.md` (the 426-line doctrine) → your scenario's strategy
  - `BENCHMARK_BASE_URL` and related platform env vars → the competition engine hard-verifies the arena API at boot (that's why configuring only a model key without a platform address yields `BENCHMARK_BASE_URL is not set`); running off the competition platform means providing or stubbing that platform interface yourself
  - model gateway & key env vars (`ANTHROPIC_BASE_URL` / `ANTHROPIC_AUTH_TOKEN` / `SAPPER_MODEL` / `SAPPER_KEY_POOL` ...) → your own model services
  - watchdog budget/deadline and report templates → adjust to your scenario
- With AI, everything is flexible — even the doctrine can be rewritten with AI's help

### Not a tool — a fruit on a tree

**sapper is not the tree; it is the first fruit the tree has borne.** The tree
is [the Nüwa Foundation](https://github.com/N1nEmAn/nvwabase) and the idea of
the Nüwa Test: give AIs the three capabilities — Create, Language, History —
plus one axiom of survival, and see what grows.

The fruit's defining trait is **evolvability**: its doctrine, ranks, and
tactics all come from "every post-mortem feeds the next legislation" — from
the competition build to the pentest edition, each generation grew stronger
than the last. It is designed to keep growing.

So open-sourcing it was never just about one more autonomous pentest tool.
The real invitation is this: **grow your own fruit on sapper-v2 or the Nüwa
Foundation.** Swap the doctrine for office teamwork, research pipelines,
software engineering — any long-horizon cooperative cause. Your scenario is
this tree's next fruit.

---

sapper is not a smarter single agent. It is a legion of AIs that divide labor,
talk to each other, and pass down what they learn: one AI commander reads the
board, decides, and dispatches; generals and soldiers attack in parallel; a
zero-strategy watchdog keeps everyone alive. All knowledge settles into a
layered fact graph — individuals die, the graph survives.

---

## 1. The Nüwa Test

Making one model ever smarter is like making one monkey ever smarter before
humans existed — however clever, it only becomes a super monkey. What turns a
 troop of monkeys into humanity is division of labor, cooperation, and
civilization.

**The Nüwa Test is the Turing test of the AGI era.** Today's large models
already pass the classic Turing test. The Nüwa Test asks the next question:

> Give an AI a si