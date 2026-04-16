# hello2cc

[![npm version](https://img.shields.io/npm/v/hello2cc.svg)](https://www.npmjs.com/package/hello2cc)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](./LICENSE)
[![Publish](https://img.shields.io/github/actions/workflow/status/hellowind777/hello2cc/publish.yml?label=publish)](https://github.com/hellowind777/hello2cc/actions/workflows/publish.yml)

Make third-party models work inside Claude Code as close to Opus as the plugin layer can drive them.

`hello2cc` does **not** replace your model gateway, provider mapping, or account permissions.  
Its job is simpler:

> If you already connected GPT, Kimi, DeepSeek, Gemini, Qwen, or other third-party models to Claude Code, `hello2cc` keeps pushing them toward Opus-compatible Claude Code behavior: native capability priorities, tool and agent choice, team/task workflow use, failure recovery, and output style.

**Language:** English | [简体中文](./README_CN.md)

---

## 🆕 What changed in 0.5.0

Compared with `0.4.9`, this release changes how `hello2cc` coexists with surfaced host skills and workflows:

| 0.5.0 note | What you should notice |
|---|---|
| Visible host skills/workflows can own the main flow | Plugins such as `superpowers` are less likely to be overridden by a parallel hello2cc playbook |
| Native output style still stays on | Even when a host workflow leads, replies remain closer to Claude Code / Opus-style presentation |
| Tool semantics and protocol adaptation remain active | Third-party models still benefit from native tool-use hints, parameter cleanup, and failure debounce |
| Session-start injected bootstrap skill docs are surfaced | `using-superpowers`-style bootstrap content can be recognized as a real host skill surface |

---

## 🎯 Why use hello2cc?

| Common problem | What hello2cc improves |
|---|---|
| A matching skill or workflow already exists, but the model keeps rewriting the process | Encourages the model to continue with the surfaced or already-loaded workflow |
| The session already exposes MCP resources or tools, but the model still takes a detour | Nudges the model toward the most direct path first |
| Plain parallel workers get confused with team or teammate semantics | Reduces avoidable agent routing mistakes |
| The model can answer, but does not pick the right Claude Code capability | Pushes tool, agent, workflow, and MCP choice back toward native Claude Code priorities |
| The model depends too much on wording or keyword hints | Switches to language-agnostic semantic matching inside host-exposed candidate boundaries |
| The output style drifts away from native Opus | Forces a tighter Claude Code-native result style |
| The model drifts into verbose meta narration | Keeps responses closer to concise native Claude Code style |

---

## ✅ Best for / ❌ Not for

### ✅ Best for

- You already use Claude Code with third-party models through **CCSwitch** or another mapping layer
- You want those models to behave more like a native Claude Code session
- You have skills, workflows, MCP servers, or plugins installed and want them to be used more reliably
- You want parallel agent work to choose a more appropriate path

### ❌ Not for

- Setting up provider accounts, API keys, or gateway access
- Exposing tools that Claude Code did not expose in the first place
- Replacing **CCSwitch**
- Overriding higher-priority repository rules such as `CLAUDE.md`, `AGENTS.md`, or direct user instructions

---

## 📊 By the numbers

| Item | Value |
|---|---|
| Install flow | 3 steps |
| Extra command required after install | 0 |
| Common config profiles | 2 |
| Main goal | 1 — make third-party models behave more like native Claude Code / Opus sessions |

---

## ✨ What it helps with

<table>
<tr>
<td width="50%">

### Skills & workflows

Better continuity when a workflow is already visible or already in progress.

</td>
<td width="50%">

### Tools & MCP

Stronger preference for capabilities that are already available in the session.

</td>
</tr>
<tr>
<td width="50%">

### Agents & teams

Keeps one-shot parallel work on ordinary agent paths, while sustained collaboration is more likely to use a real team + task-board flow.

</td>
<td width="50%">

### Cleaner interaction

Less unnecessary meta narration and fewer avoidable routing mistakes.

</td>
</tr>
</table>

---

## 🚀 Quick start

### 1) Clone this repository

```bash
git clone https://github.com/hellowind777/hello2cc.git
cd hello2cc
```

### 2) Add the local marketplace

```bash
claude plugins marketplace add "<repo-path>"
```

Replace `<repo-path>` with your local `hello2cc` repository path.

### 3) Install the plugin

```bash
claude plugins install hello2cc@hello2cc-local
```

Then reopen Claude Code or run `/reload-plugins`.

### Expected result

- No extra manual entry point is required
- Installing the plugin does not write `agent=hello2cc:native` into Claude Code settings
- Plugin enablement stays under Claude Code's own plugin state, not a plugin-shipped `settin