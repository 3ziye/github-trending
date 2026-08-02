<p align="center">
  <img src="assets/banner.png" alt="Engram — learn anything. keep it." width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.10.1-6D4AA8.svg" alt="Version 1.10.1">
  <a href="https://www.npmjs.com/package/opencode-engram-learning"><img src="https://img.shields.io/npm/v/opencode-engram-learning?label=npm&color=6D4AA8" alt="npm package"></a>
  <img src="https://img.shields.io/badge/license-MIT-yellow.svg" alt="MIT License">
  <img src="https://img.shields.io/badge/selftest-302%2F302-3E7D5A.svg" alt="302/302 checks">
  <a href="gold/assessor-gold.jsonl"><img src="https://img.shields.io/badge/grader%20inflations-0%2F258-3E7D5A.svg" alt="0 of 258 blind judgments graded up, on the shipping spec"></a>
  <img src="https://img.shields.io/badge/scheduler-FSRS--4.5-6D4AA8.svg" alt="FSRS-4.5">
  <a href="CONTRIBUTING-DATA.md"><img src="https://img.shields.io/badge/data-100%25%20local-3E7D5A.svg" alt="100% local — the engine has no network code, proven by a permanent selftest"></a>
  <a href="https://discord.gg/temm1e"><img src="https://img.shields.io/badge/discord-community-5865F2.svg" alt="Discord community"></a>
</p>

<h3 align="center">Your AI can explain anything. Engram makes sure <em>you</em> still know it next month.</h3>

> **The mix-up worth clearing first: Engram is not an agent-memory plugin.** It doesn't give your agent persistent memory, context, or knowledge of your codebase — memory MCPs and context tools do that, *for the agent*. Engram points the other way: **it's a learning system for the human.** Your agent becomes a tutor that makes you do the thinking, a blind examiner that checks you actually got it, and a scheduler that brings each idea back right before your brain drops it. The agent doesn't get smarter. **You do — measurably, with receipts.**

Born as a Claude Code plugin; the same skills and engine now run on six agentic platforms — including, as of v1.0.8, one that puts the tutor in your chat app:

```bash
claude plugin marketplace add nagisanzenin/engram
claude plugin install engram@engram
```

| Platform | Install | Then |
|---|---|---|
| **Claude Code** (born here) | the two commands above | `/learn` `/review` `/coach` |
| **OpenAI Codex** | `codex plugin marketplace add nagisanzenin/engram` then `codex plugin add engram@engram` → [INSTALL-CODEX.md](INSTALL-CODEX.md) | `$learn` `$review` `$coach` |
| **OpenCode** | `"plugin": ["opencode-engram-learning"]` in `opencode.json` ([npm](https://www.npmjs.com/package/opencode-engram-learning)) | `/learn` `/review` `/coach` |
| **Hermes Agent** | clone + `skills.external_dirs` → [INSTALL-HERMES.md](INSTALL-HERMES.md) — verified live on v0.18.2 | `/skill learn` (or `/study`) `/review` `/coach` |
| **Google Antigravity** | `agy plugin install https://github.com/nagisanzenin/engram` | `/learn` `/review` `/coach` |
| **OpenClaw** | `openclaw plugins install engram --marketplace nagisanzenin/engram` → [INSTALL-OPENCLAW.md](INSTALL-OPENCLAW.md) — verified on 2026.7.1-2 | `/learn` `/review` `/coach` |

<sub>OpenCode: `opencode.json` is read globally (`~/.config/opencode/opencode.json`) or per-project; pin to source instead of npm with `"plugin": ["git+https://github.com/nagisanzenin/engram.git"]`.</sub><br>
<sub>Antigravity: The due-review session nudge isn't ported yet, and the `architect` and `smith` subagents are currently dropped by AG 1.1.4's strict installer. Everything else works the same.</sub><br>
<sub>OpenClaw: the nudge needs `openclaw config set hooks.internal.enabled true` (OpenClaw ignores plugin hooks until internal hooks are switched on), and it fires on `/new` and `/reset` rather than every session. Engram's agents aren't registered — the skills spawn them through `sessions_spawn` with isolated context instead, which keeps the assessor blind. Details in [INSTALL-OPENCLAW.md](INSTALL-OPENCLAW.md).</sub>

Then, inside your coding assistant (command spelling per your platform's row above):

```
/learn kalman filters        ← or music theory, or Rust lifetimes, or anything
```

That's the whole onboarding. No config, no account, no cards to write. Requires `python3` (stock macOS/Linux one is fine — stdlib only). One state folder, every platform: learn in one tool, review in another, same schedule.

---

## Wait — what *is* this?

You already ask Claude to explain things. It explains beautifully. You nod, you feel smart, and **ten days later it's gone** — because a chat has no memory of you, no test of whether you really got it, and no plan for the forgetting that starts the moment you close the terminal.

Engram is what's missing around the explanation: **a tutor that makes you do the thinking, an examiner that checks you actually got it, and a scheduler that brings each idea back right before your brain drops it.**

| Engram **is** | Engram is **not** |
|---|---|
| **a learning system for the human — *you* end up knowing things** | **agent memory — tools that persist what the *agent* kn