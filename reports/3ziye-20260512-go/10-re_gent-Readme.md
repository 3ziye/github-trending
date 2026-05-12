<div align="center">
  <a href="https://github.com/regent-vcs/regent">
    <img
      src="assets/regent-logo-dark.png"
      alt="re_gent"
      width="100%"
    />
  </a>
  <br />
  <br />
  <h1>Version-Control for AI Agents</h1>
  <p>
    Version control for AI agent activity. Track what your agent did, which prompt wrote each line, and rewind when things break.
  </p>

[![Star on GitHub](https://img.shields.io/github/stars/regent-vcs/regent?style=for-the-badge&logo=github&color=gold)](https://github.com/regent-vcs/regent)
[![Apache 2.0 License](https://img.shields.io/badge/License-Apache%202.0-blue?style=for-the-badge)](LICENSE)
[![Go Version](https://img.shields.io/github/go-mod/go-version/regent-vcs/regent?style=for-the-badge&logo=go&logoColor=white&color=00ADD8)](go.mod)

[![CI Status](https://img.shields.io/github/actions/workflow/status/regent-vcs/regent/ci.yml?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/regent-vcs/regent/actions/workflows/ci.yml)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-10b981?style=for-the-badge&logo=github)](CONTRIBUTING.md)
[![Claude Code Compatible](https://img.shields.io/badge/Claude%20Code-Compatible-6366f1?style=for-the-badge&logo=anthropic&logoColor=white)](https://github.com/regent-vcs/regent)

</div>

---

## Demo

<div align="center">
  <img src="assets/demo-fast.gif" alt="re_gent tracking Claude Code activity" width="100%"/>
  <p><em>Every tool call is automatically captured. No manual commits needed.</em></p>
</div>

---

## Quick Start

```bash
# Install via Homebrew (macOS/Linux)
brew tap regent-vcs/tap
brew install regent

# Or via Go
go install github.com/regent-vcs/regent/cmd/rgt@latest

# Initialize in your project
cd your-project
rgt init

# Work with Claude Code normally (every tool call is tracked)

# See what happened
rgt log
rgt blame src/file.go:42
```

That's it. Your agent activity is now auditable.

---

## What You Get

### See what your agent actually did

```bash
$ rgt log

Step a1b2c3d  |  2 min ago  |  Tool: Edit
│ File: src/handler.go
│ Added error handling to request handler
│ + 5 lines, - 2 lines

Step d4e5f6g  |  5 min ago  |  Tool: Write
│ File: tests/handler_test.go
│ Created unit tests for handler
│ + 23 lines

Step f8g9h0i  |  8 min ago  |  Tool: Bash
│ Command: go mod tidy
│ Cleaned up dependencies
```

### Blame: which prompt wrote this line?

```bash
$ rgt blame src/handler.go:42

Line 42: func handleRequest(w http.ResponseWriter, r *http.Request) {

Step:    a1b2c3d4e5f6
Session: claude-20260502-143021
Tool:    Edit
Prompt:  "Add error handling to the request handler"
```

### Track multiple concurrent sessions

```bash
$ rgt sessions

Active Sessions:
claude-20260502-143021  |  3 steps  |  Last: 2 min ago
claude-20260502-091534  |  7 steps  |  Last: 2 hours ago

$ rgt log --session claude-20260502-143021
# Filter history by session
```

### See full context for any change

```bash
$ rgt show a1b2c3d

Step a1b2c3d4e5f6
Parent: d4e5f6g7h8i9
Session: claude-20260502-143021
Time: 2026-05-02 14:30:21

Tool: Edit
File: src/handler.go

Changes:
+ func handleRequest(w http.ResponseWriter, r *http.Request) {
+     if r.Method != "GET" {
+         http.Error(w, "Method not allowed", 405)
+         return
+     }
- func handleRequest(w http.ResponseWriter, r *http.Request) {

Conversation:
User: "Add error handling to reject non-GET requests"
Assistant: "I'll add method validation to the handler..."
```

---

## Why This Exists

**The problem:** AI agents have no version control of their own.

You know this pain:
- *"It was working five minutes ago"*
- *"Why did you change that file?"*
- *"Go back to before the refactor"*
- `/compact` and pray
- Copy-pasting code into a fresh chat

**The solution:** Three primitives that should already exist:

- **`rgt log`** — what did this session do?
- **`rgt blame`** — which prompt wrote this line?
- **`rgt rewind`** — restore to any previous step (coming soon)

We gave agents write access to our codebases. We did not give ourselves git for it. re_gent fixes that.

---

## How It Works

re_gent stores agent activity in `.regent/` (like `.git/`):

```
.regent/
├── objects/     # Content-addressed blobs (BLAKE3)
├── refs/        # Session pointers (one per agent)
├── index.db     # SQLite query index
└── config.toml
```

Every tool call creates a **Step**:

```go
Step {
  parent:      <previous-step-hash>
  tree:        <workspace-snapshot>
  transcript:  <conversation-delta>
  cause: {
    tool_name: "Edit"
    args:      <what-changed>
    result:    <tool-output>
  }
  session_id:  "claude-20260502-143021"
  timestamp:   "2026-05-02T14:30:21Z"
}
```

Steps form a **DAG**. Each session has its own branch. Common ancestors dedupe. You get git-level auditability for agent activity.

**Technical details:** See [POC.md](POC.md) for the complete specification.

---

## Installation

### Via Homebrew (macOS/Linux)

```bash
brew tap regent-vcs/tap
b