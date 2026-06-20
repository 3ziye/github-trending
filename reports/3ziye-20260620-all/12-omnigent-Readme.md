<div align="center">

# <img src="https://raw.githubusercontent.com/omnigent-ai/omnigent/main/docs/images/omnigent-logo.svg" alt="" height="38" valign="middle" /> Omnigent

### The open-source AI agent framework and meta-harness for all your AI agents.

Omnigent is an open-source **AI agent framework** and meta-harness that gives you a common orchestration layer over Claude Code, Codex, Cursor, Pi, and the agents you write yourself: swap or combine harnesses without rewriting, enforce policies and sandboxing, and collaborate in real time from any device.

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://github.com/omnigent-ai/omnigent/blob/main/LICENSE)
![Status: alpha](https://img.shields.io/badge/status-alpha-orange.svg)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue.svg)](#1-install)

[omnigent.ai](https://omnigent.ai) · **[⬇️ Download the macOS desktop app](https://omnigent.ai/download/mac)**

</div>

<p align="center">
  <img src="https://raw.githubusercontent.com/omnigent-ai/omnigent/main/docs/images/omnigent-hero.png" alt="An Omnigent orchestrator and its sub-agents in one shared session" width="520" />
</p>

---

## Why Omnigent?

Omnigent lets you:

- **📱 Work with agents from any device, including your phone.** Sessions
  follow you: start in your terminal, continue in the browser, pick it up on
  your phone. Messages, sub-agents, terminals, and files stay in sync.

- **🤖 Supervise multiple agents.** Use Claude Code, Codex, Pi, and custom
  agents (defined in YAML) together in the same session. Ask one agent to
  review another's work, or split a task across agents that are each good at
  different things.

- **🔌 Use any model.** A first-party API key, a Claude/ChatGPT subscription,
  or any compatible gateway. All first-class.

- **🤝 Collaborate.** Share a session so teammates can chat with your agent
  and watch it work live, co-drive it on your machine, or fork the
  conversation to continue on their own.

- **☁️ Run agents in cloud sandboxes.** No laptop required: run sessions in
  disposable [Modal](https://modal.com), [Daytona](https://www.daytona.io), or
  [Islo](https://islo.dev) sandboxes, launched from the CLI or provisioned by
  the server per session (*managed hosts*).

- **🛡️ Govern your agents.** Create
  [policies](#6-govern-your-agents-with-policies) to pause for your approval
  before risky actions, cap spend, or limit which tools an agent reaches.
  They apply to the whole server, one agent, or a single chat.

---

## Quick start

### 1. Install

One command installs Omnigent and everything it needs:

```bash
curl -fsSL https://raw.githubusercontent.com/omnigent-ai/omnigent/main/scripts/install_oss.sh | sh
```

<details>
<summary>Prefer to install manually?</summary>

Omnigent needs **Python 3.12+**. Install the `omnigent` package:

```bash
uv tool install omnigent        # or: pip install "omnigent"
```

Or with [Homebrew](https://github.com/omnigent-ai/homebrew-tap):

```bash
brew install omnigent-ai/tap/omnigent
```

Or install straight from the repo:

```bash
uv tool install -q --python 3.12 git+https://github.com/omnigent-ai/omnigent.git
```

</details>

<details>
<summary>Toolchain and prerequisites (if the installer reports a missing tool)</summary>

- **`uv`** (required). https://docs.astral.sh/uv/getting-started/installation/
  The installer offers to set this up for you.
- **`git`** (required).
- **Node.js 22 LTS or newer** with **`npm`**, for the Claude, Codex, and Pi
  coding harnesses. `omnigent run` installs the harness CLI you pick.
  https://docs.npmjs.com/downloading-and-installing-node-js-and-npm
- **`tmux`**, required by the native `omnigent claude` / `omnigent codex`
  wrappers (`brew install tmux` / `apt install tmux`; the installer offers
  to install it for you).
- **`bubblewrap`** (`bwrap`), **Linux only**. The native `omnigent claude` /
  `omnigent codex` and `pi` harnesses wrap each agent terminal in a `bwrap`
  OS-sandbox; on Linux that isolation is mandatory, so a missing `bwrap`
  binary makes those terminals fail to start (`apt install bubblewrap`; the
  installer offers to install it for you). macOS uses the built-in `seatbelt`
  sandbox and needs nothing extra.
- **Databricks** (optional). To use a Databricks workspace as your model
  provider, install Omnigent with the `databricks` extra:
  `uv tool install "omnigent[databricks]"` — or pass it to the bootstrap
  installer with `... | sh -s -- --extra databricks`. Signing in to the
  workspace also uses the [Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli/install).

</details>

<details>
<summary>Updating to a new release</summary>

When a newer release is on PyPI, Omnigent shows a one-line notice (once per
release) pointing here. To update:

```bash
omni upgrade            # detects how you installed, drains & stops the local
                        # server, then runs the matching upgrade command
omni upgrade --check   