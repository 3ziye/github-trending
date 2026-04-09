<p align="center">
  <img src="assets/tray-icon.png" width="128" alt="Clawd">
</p>
<h1 align="center">Clawd on Desk</h1>
<p align="center">
  <a href="README.zh-CN.md">中文版</a>
</p>

A desktop pet that reacts to your AI coding agent sessions in real-time. Clawd lives on your screen — thinking when you prompt, typing when tools run, juggling subagents, reviewing permissions, celebrating when tasks complete, and sleeping when you're away.

> Supports Windows 11, macOS, and Ubuntu/Linux. Requires Node.js. Works with **Claude Code**, **Codex CLI**, **Copilot CLI**, **Gemini CLI**, **Cursor Agent**, **Kiro CLI**, and **opencode**.

## Features

### Multi-Agent Support
- **Claude Code** — full integration via command hooks + HTTP permission hooks
- **Codex CLI** — automatic JSONL log polling (`~/.codex/sessions/`), no configuration needed
- **Copilot CLI** — command hooks via `~/.copilot/hooks/hooks.json`
- **Gemini CLI** — command hooks via `~/.gemini/settings.json` (registered automatically when Clawd starts, or run `npm run install:gemini-hooks`)
- **Cursor Agent** — [Cursor IDE hooks](https://cursor.com/docs/agent/hooks) in `~/.cursor/hooks.json` (registered automatically when Clawd starts, or run `npm run install:cursor-hooks`)
- **Kiro CLI** — command hooks injected into custom agent configs under `~/.kiro/agents/`, plus an auto-created `clawd` agent that is re-synced from Kiro's built-in `kiro_default` whenever Clawd starts, so you can opt into hooks with minimal behavior drift via `kiro-cli --agent clawd` or `/agent swap clawd` (registered automatically when Clawd starts, or run `npm run install:kiro-hooks`). State hooks have been verified on macOS.
- **opencode** — [plugin integration](https://opencode.ai/docs/plugins) via `~/.config/opencode/opencode.json` (registered automatically when Clawd starts); zero-latency event streaming, permission bubbles with Allow/Always/Deny, and building animations when parallel subagents are spawned via the `task` tool
- **Multi-agent coexistence** — run all agents simultaneously; Clawd tracks each session independently

### Animations & Interaction
- **Real-time state awareness** — agent hooks and log polling drive Clawd's animations automatically
- **12 animated states** — idle, thinking, typing, building, juggling, conducting, error, happy, notification, sweeping, carrying, sleeping
- **Eye tracking** — Clawd follows your cursor in idle state, with body lean and shadow stretch
- **Sleep sequence** — yawning, dozing, collapsing, sleeping after 60s idle; mouse movement triggers a startled wake-up animation
- **Click reactions** — double-click for a poke, 4 clicks for a flail
- **Drag from any state** — grab Clawd anytime (Pointer Capture prevents fast-flick drops), release to resume
- **Mini mode** — drag to right edge or right-click "Mini Mode"; Clawd hides at screen edge with peek-on-hover, mini alerts/celebrations, and parabolic jump transitions

### Permission Bubble
- **In-app permission review** — when Claude Code requests tool permissions, Clawd pops a floating bubble card instead of waiting in the terminal
- **Allow / Deny / Suggestions** — one-click approve, reject, or apply permission rules (e.g. "Always allow Read")
- **Global hotkeys** — `Ctrl+Shift+Y` to Allow, `Ctrl+Shift+N` to Deny the latest permission bubble (only registered while bubbles are visible)
- **Stacking layout** — multiple permission requests stack upward from the bottom-right corner
- **Auto-dismiss** — if you answer in the terminal first, the bubble disappears automatically

### Session Intelligence
- **Multi-session tracking** — sessions across all agents resolve to the highest-priority state
- **Subagent awareness** — juggling for 1 subagent, conducting for 2+
- **Terminal focus** — right-click Clawd → Sessions menu to jump to a specific session's terminal window; notification/attention states auto-focus the relevant terminal
- **Process liveness detection** — detects crashed/exited agent processes (Claude Code, Codex, Copilot) and cleans up orphan sessions
- **Startup recovery** — if Clawd restarts while any agent is running, it stays awake instead of falling asleep

### System
- **Click-through** — transparent areas pass clicks to windows below; only Clawd's body is interactive
- **Position memory** — Clawd remembers where you left it across restarts (including mini mode)
- **Single instance lock** — prevents duplicate Clawd windows
- **Auto-start** — Claude Code's SessionStart hook can launch Clawd automatically if it's not running
- **Do Not Disturb** — right-click or tray menu to enter sleep mode; all hook events are silenced until you wake Clawd. Permission bubbles are suppressed during DND — opencode falls back to its built-in TUI prompt, and Claude Code will handle permissions automatically
- **Sound effects** — short audio cues on task completion and permission requests (toggle via right-click menu; 10s cooldown, auto-muted during DND)
- **System tray** — resize (S/M/L), DND mode,