<p align="center"><img src="docs/icon.png" width="96" alt="Chrome Relay icon"></p>

# Chrome Relay

<p align="center">
  <a href="https://agent-chrome-relay.aindeev.com"><img alt="Website" src="https://img.shields.io/badge/website-agent--chrome--relay.aindeev.com-0b0d10?style=flat-square"></a>
  <a href="https://read.aindeev.com"><img alt="Blog: The Leveraged Mind" src="https://img.shields.io/badge/blog-The%20Leveraged%20Mind-ff6719?style=flat-square&logo=substack&logoColor=white"></a>
  <a href="https://x.com/AlexeyIndeev"><img alt="X: @AlexeyIndeev" src="https://img.shields.io/badge/X-@AlexeyIndeev-000000?style=flat-square&logo=x&logoColor=white"></a>
  <a href="https://www.linkedin.com/in/alexey-indeev/"><img alt="LinkedIn: Alexey Indeev" src="https://img.shields.io/badge/LinkedIn-Alexey%20Indeev-0a66c2?style=flat-square&logo=linkedin&logoColor=white"></a>
  <a href="LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-2ea44f?style=flat-square"></a>
</p>

<p align="center">
  <a href="https://testflight.apple.com/join/zhpm8gND"><img alt="iPhone app: join the beta on TestFlight" src="https://img.shields.io/badge/iPhone%20app-Join%20the%20beta%20on%20TestFlight-0d96f6?style=for-the-badge&logo=apple&logoColor=white"></a>
</p>

Lets your coding agents (Claude Code, Codex, Cursor, Paseo, pi) use **your everyday Chrome**, with your real
logins, from the command line, **in background tabs**: nothing takes focus, nothing on your screen moves.

- **Whole goals in one command.** `chrome-relay do "Invite the new teammate as an admin" --data "Email=ada@example.com"
  --until "text:Invitation sent"` fills, clicks and checks every step, in about the time an agent spends on one
  click. [More](#whole-goals-in-one-command-chrome-relay-do)
- **Or step by step**, with checked commands that answer in tens of milliseconds (`open`, `snapshot`, `click`,
  `fill`). [More](#step-by-step-chrome-relays-own-commands)
- **Sign-ins without you.** Google account hops are clicked through; other logins come from the 1Password vaults
  you share with it (passwords, 2-step codes, passkeys), typed by Chrome Relay so the agent never sees them.
  [More](#signing-in-with-1password-optional)
- **Approvals on your iPhone** when you're away from the Mac, with Face ID. [More](#approving-from-your-iphone)
- **An audit trail** of everything every agent did. [More](#audit-trail)

<p align="center"><img src="docs/readme/1password-sign-in.png" width="900" alt="An agent fills a Twilio login with op:// references; Chrome Relay asks with Touch ID, naming the agent, site, account and item, and the agent's snapshot shows only dots"></p>

**Status**
- **Mac service:** built from source on your Mac ([Setup](#setup-once-per-mac-2-minutes), about 2 minutes).
- **Chrome extension:** [in the Chrome Web Store](https://chromewebstore.google.com/detail/mdglmmedlbkjphgolcejpphnbclkfnom)
  (unlisted: only at that link).
- **iPhone app**, Chrome Relay Approve: [on TestFlight](https://testflight.apple.com/join/zhpm8gND) (install
  TestFlight on the iPhone, then open the link there); in App Store review.
- **Password managers:** 1Password only, for now.

**The core** is background tabs with your logins, `chrome-relay do`, Google sign-in hops and an audit trail.
**Everything else is optional** and off until you turn it on: 1Password, Secure Enclave passkeys, iPhone
approvals, and a TypeSafe key for the fastest decider. See [What's optional](#whats-optional). Nothing installs
the extension for you, and it only runs on Macs whose owner set it up.

## How it works

```
chrome-relay open/click/fill/... ──unix socket /driver──┐
chrome-relay do ──────────────────unix socket /driver───┼──▶ relay (127.0.0.1:9333, LaunchAgent) ──ws──▶ Chrome Relay extension ──chrome.debugger──▶ agent tab
agent-browser (optional) ─────────ws (DevTools)─────────┘         ▲
   │                                                               └── reads the page and acts, in that agent's own tabs only
   └── do decides: saved flows → the agent's data → Jev or Haiku (Claude Code) → hand back to the agent
```

- **Extension** (`extension/`, MV3, one per Chrome profile you load it in): opens each agent tab **inactive**
  in a collapsed "Agents" tab group and runs DevTools commands in it via `chrome.debugger`. No remote-debugging
  port, so Chrome never shows "Allow remote debugging?". Chrome does show "Chrome Relay started debugging this
  browser" while agents work.
- **`chrome-relay`**: one Go program, **built and signed on your own Mac** (`./build`). As a background service
  (`chrome-relay serve`) it is the relay: a DevTools endpoint per agent, where each agent sees and controls only
  the tabs it opened and commands that could raise or focus the browser are swallowed. It is also the CLI
  (setup, the connection URL, `do`, diagnostics, audit trail), and the optional 1Password vault and passkeys, whose
  Secure Enclave and Touch ID code (`internal/macos`, Swift) is linked into 