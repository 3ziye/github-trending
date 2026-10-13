<p align="center"><img src="docs/icon.png" width="96" alt="Chrome Relay icon"></p>

# Chrome Relay

<p align="center">
  <a href="https://agent-chrome-relay.aindeev.com"><img alt="Website" src="https://img.shields.io/badge/website-agent--chrome--relay.aindeev.com-0b0d10?style=flat-square"></a>
  <a href="https://read.aindeev.com"><img alt="Blog: The Leveraged Mind" src="https://img.shields.io/badge/blog-The%20Leveraged%20Mind-ff6719?style=flat-square&logo=substack&logoColor=white"></a>
  <a href="https://x.com/AlexeyIndeev"><img alt="X: @AlexeyIndeev" src="https://img.shields.io/badge/X-@AlexeyIndeev-000000?style=flat-square&logo=x&logoColor=white"></a>
  <a href="https://www.linkedin.com/in/alexey-indeev/"><img alt="LinkedIn: Alexey Indeev" src="https://img.shields.io/badge/LinkedIn-Alexey%20Indeev-0a66c2?style=flat-square&logo=linkedin&logoColor=white"></a>
  <a href="LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-2ea44f?style=flat-square"></a>
</p>

**Website:** https://agent-chrome-relay.aindeev.com


Lets your coding agents (Claude Code, Codex, Cursor, Paseo) use **your everyday Chrome**, with your real
logins, from the command line, **in background tabs**: nothing takes focus, no dialogs.

Agents hand over **a whole goal in one command**, and Chrome Relay carries it out, checking every step:

```bash
agent-browser --cdp "$(chrome-relay url you@company.com)" open https://app.example.com/team/invite
chrome-relay do "Invite the new teammate as an admin" \
  --data "Email=ada@example.com" --data "Role=Admin" --until "text:Invitation sent"
```

It fills what the agent names, replays what worked on that site before, asks a fast decision model (TypeSafe's
Jev, or Claude Haiku through your own Claude Code) only for real choices, and hands back anything it isn't sure of.
In a real Chrome with Jev: a 7-step form in **2.5 s**, **1.2 s** replayed, where an agent clicking step by step
takes about 3 s per action. See [`chrome-relay do`](#whole-goals-in-one-command-chrome-relay-do) and
[the approach](https://agent-chrome-relay.aindeev.com/approach.html).

Step by step works too, at ~0.15 s per command:

```bash
agent-browser snapshot -i          # the page's buttons, links and fields, each with a ref like @e5
agent-browser click @e5
agent-browser close
```

It's opt-in: nothing installs the extension for you, and it only runs on Macs whose owner set it up.

**Status.** Today you build Chrome Relay from source (below). The Chrome extension is in Chrome Web Store review and
the iPhone app, Chrome Relay Approve, is in App Store review: both are coming soon, and until then you load the
extension from your clone and build the iPhone app with Xcode. Signing in with a password manager works with
**1Password only** for now.

**The core** is background tabs with your logins, `chrome-relay do`, Google sign-in hops and an audit trail.
**Everything else is optional** and off until you turn it on: signing in with 1Password (passwords, 2-step codes,
passkeys), Secure Enclave passkeys, approving from your iPhone, and a TypeSafe key for the fastest decider. See
[What's optional](#whats-optional).

## How it works

```
agent-browser (CLI) ──ws──────────────┐
                                      ├──▶ relay (127.0.0.1:9333, LaunchAgent) ──ws──▶ Chrome Relay extension ──chrome.debugger──▶ agent tab
chrome-relay do ──http /driver────────┘         ▲
   │                                            └── reads the page and acts, in that agent's own tabs only
   └── decides: saved flows → the agent's data → Jev or Haiku (Claude Code) → hand back to the agent
```

- **Extension** (`extension/`, MV3, one per Chrome profile you load it in): opens each agent tab **inactive**
  in a collapsed "Agents" tab group and runs DevTools commands in it via `chrome.debugger`. No remote-debugging
  port, so Chrome never shows "Allow remote debugging?". Chrome does show "Chrome Relay started debugging this
  browser" while agents work.
- **`chrome-relay`**: one Go program, **built and signed on your own Mac** (`./build`). As a background service
  (`chrome-relay serve`) it is the relay: a DevTools endpoint per agent, where each agent sees and controls only
  the tabs it opened and commands that could raise or focus the browser are swallowed. It is also the CLI
  (setup, the connection URL, `do`, diagnostics, audit trail), and the optional 1Password vault and passkeys, whose
  Secure Enclave and Touch ID code (`internal/macos`, Swift) is linked into the same signed binary when Xcode's
  command line tools are installed.

## Setup (once per Mac, ~2 minutes)

Fastest: paste [this prompt](https://agent-chrome-relay.aindeev.com/setup-prompt.txt) into Claude Code, Codex or
Cursor in its auto mode (Claude Code: Shift+Tab, or `claude --permission-mode auto`; Codex:
`--full-auto`) and let your agent do it. You only load the extension and approve in 1Password. By hand:

Needs macOS, Google Chrome, [Go](https://go.dev/dl/) 1.25+ (`brew in