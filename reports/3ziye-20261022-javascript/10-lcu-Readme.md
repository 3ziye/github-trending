<p align="center">
  <img src="docs/assets/lcu-icon.svg" width="120" height="120" alt="LCU logo">
</p>

<h1 align="center">LCU</h1>

<p align="center"><strong>Codex computer use, decoupled from the Codex app.</strong></p>

https://github.com/user-attachments/assets/bd9d0809-8a6c-4931-a51c-b98daf05cb5f

LCU exposes Codex's original computer-use runtime to your harness without requiring Codex authentication. The official ChatGPT desktop app must still be installed locally: it supplies the runtime and instructions, while LCU handles setup and harness integration.

## Quick start

Copy this into your agent:

```text
Install and configure LCU for this harness using the latest release.
Follow https://raw.githubusercontent.com/amontlabs/lcu/main/docs/INSTALLATION.md
Check my OS, architecture, and prerequisites, then guide me through any required permissions.
```

In Claude Code on an Apple Silicon Mac, two commands do the same through its plugin manager; see [Claude Code plugin](docs/INSTALLATION.md#claude-code-plugin):

```sh
claude plugin marketplace add amontlabs/lcu
claude plugin install lcu@lcu
```

## Features

- **Desktop apps:** read windows, click, type, and take screenshots.
- **Chrome, when enabled:** read and control tabs through the official extension, with site approval.
- **In your harness:** adapters are available for Pi, Codex CLI, and Claude Code, with experimental Oh My Pi, Hermes and DeepSeek Harness integrations. See [setup and verification limits](docs/ADAPTERS.md).

## Approve apps from Claude, natively

The first time an agent controls an app (Zed, Notes, Safari), the computer-use runtime asks you to allow it. The Claude app's Code tab used to fail that request with "Computer Use was not approved". `lcu setup --agent claude-code` now installs a small Claude Code mod, `lcu-approve`, that asks the question natively: as a question card in the Claude app, which flags the session as needing input, and as a **Computer use approval** pane in the terminal.

<p align="center"><img src="docs/assets/approval-demo.gif" width="720" alt="The Computer use approval pane in Claude Code: Allow this conversation, a high-risk app with its warning, and the Approved apps panel"></p>

- **Allow this conversation** for the current chat only.
- **Always allow** to remember the app (offered only when the runtime allows it).
- **Deny** to refuse.

The `/computer-use-apps` command opens an **Approved apps** panel in the same place: one line per always-allowed app with Revoke (macOS asks for Touch ID or your password), apps that are no longer installed grouped below, this conversation's grants, and an Allow field.

Only you can answer: the model cannot see, press or fake the pane. High-risk apps show the runtime's own warning (reworded to say "computer use" and "the agent"), and the app hosting the agent is never approved. Needs the Claude app or Claude Code 2.1.287+. [How it works](docs/ADAPTERS.md#native-app-approvals-in-claude-code-and-the-claude-app), [how to remove it](docs/INSTALLATION.md#uninstall).

In the Claude app, register LCU through Claude Code (`lcu setup --agent claude-code`), not through Settings > Connectors; see [installation](docs/INSTALLATION.md#native-approvals-in-the-claude-app).

## Manage approved apps with Touch ID

"Always allow" is remembered. Review and change that list from the terminal (macOS), without opening the Codex app:

```sh
lcu apps                 # what is always allowed today
lcu apps allow Zed       # Touch ID (or your password), then Zed is allowed
lcu apps revoke Zed      # take it back
```

<p align="center"><img src="docs/assets/approved-apps.png" width="720" alt="The Approved apps panel opened with /computer-use-apps"></p>

- Pass an app name, a bundle identifier or an `.app` path.
- Listing is free; `allow` and `revoke` need you at the machine, so an agent running them is stopped by the prompt.
- Running sessions pick the change up immediately.
- Browsers, password managers and other high-risk apps come with a warning; apps Computer Use refuses outright (Terminal, iTerm2) are declined.

[Details](docs/INSTALLATION.md#manage-approved-apps).

## Keep Computer Use across turns (Claude Code)

In Claude Code, Computer Use normally ends with the turn that started it. A background subagent still working after that turn ended, or a turn that reuses an ended turn id, is told "Computer Use is unavailable because the current turn ended." An opt-in setting keeps it available for every turn of the session:

```sh
lcu cross-turn           # status
lcu cross-turn on        # Touch ID (or your password) on macOS
lcu cross-turn off       # no prompt
```

- Off by default. `lcu setup --cross-turn on|off` sets it too; interactive setup asks once.
- It affects only the Claude Code relay; Codex, Pi, Oh My Pi and Hermes ignore it. Per-app approvals (macOS and Windows) and your harness's tool approvals still apply.
- A foreground subagent finishing no longer ends the parent's Computer Use, wit