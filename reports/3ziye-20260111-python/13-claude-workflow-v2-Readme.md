# project-starter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-v1.0.33+-blue.svg)](https://code.claude.com)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/CloudAI-X/claude-workflow/pulls)

A universal Claude Code workflow plugin with specialized agents, skills, hooks, and output styles for any software project.

---

## Quick Start

### Option 1: CLI (Per-Session)

```bash
# Clone the plugin
git clone https://github.com/CloudAI-X/claude-workflow.git

# Run Claude Code with the plugin
claude --plugin-dir ./claude-workflow
```

### Option 2: Agent SDK

```typescript
import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const message of query({
  prompt: "Hello",
  options: {
    plugins: [{ type: "local", path: "./claude-workflow" }],
  },
})) {
  // Plugin commands, agents, and skills are now available
}
```

### Option 3: Install Permanently

```bash
# Install from marketplace (when available)
claude plugin install project-starter

# Or install from local directory
claude plugin install ./claude-workflow
```

### Verify Installation

After loading the plugin, verify it's working:

```
> /plugin
```

Tab to **Installed** - you should see `project-starter` listed.
Tab to **Errors** - should be empty (no errors).

These commands become available:

```
/project-starter:architect    # Architecture-first mode
/project-starter:rapid        # Ship fast mode
/project-starter:commit       # Auto-generate commit message
/project-starter:verify-changes  # Multi-agent verification
```

---

## What's Included

| Component    | Count | Description                                                              |
| ------------ | ----- | ------------------------------------------------------------------------ |
| **Agents**   | 7     | Specialized subagents for code review, debugging, security, etc.         |
| **Commands** | 17    | Slash commands for workflows and output styles                           |
| **Skills**   | 6     | Knowledge domains Claude uses autonomously                               |
| **Hooks**    | 9     | Automation scripts for formatting, security, verification, notifications |

---

## Usage Examples

### Commands in Action

**Auto-commit your changes:**

```
> /project-starter:commit

Looking at staged changes...
✓ Created commit: feat(auth): add JWT refresh token endpoint
```

**Full git workflow:**

```
> /project-starter:commit-push-pr

✓ Committed: feat: add user dashboard
✓ Pushed to origin/feature/dashboard
✓ Created PR #42: https://github.com/you/repo/pull/42
```

**Verify before shipping:**

```
> /project-starter:verify-changes

Spawning verification agents...
├─ build-validator: ✓ Build passes
├─ test-runner: ✓ 42 tests pass
├─ lint-checker: ⚠ 2 warnings (non-blocking)
└─ security-scanner: ✓ No vulnerabilities

Ready to ship!
```

### Agents in Action

Agents spawn automatically based on your request:

**You say:** "The login is broken, users get 401 errors"

```
[debugger agent activated]
→ Checking auth middleware... found issue
→ Token validation uses wrong secret in production
→ Fix: Update AUTH_SECRET in .env.production
```

**You say:** "Review my changes"

```
[code-reviewer agent activated]
→ Analyzing 3 files changed...
✓ Logic is correct
⚠ Missing null check on line 42
⚠ Consider adding rate limiting to this endpoint
```

**You say:** "Add authentication to the API"

```
[orchestrator agent activated]
→ Breaking down into subtasks:
  1. Design auth schema (spawning architect)
  2. Implement JWT middleware
  3. Add login/register endpoints
  4. Write tests (spawning test-architect)
  5. Update API docs (spawning docs-writer)
```

### Skills in Action

Skills provide domain knowledge automatically:

**You ask:** "How should I structure the payment service?"

```
[designing-architecture skill applied]
→ Recommending hexagonal architecture
→ Payment providers as adapters
→ Core domain isolated from infrastructure
```

**You ask:** "Make this endpoint faster"

```
[optimizing-performance skill applied]
→ Adding database indexes
→ Implementing response caching
→ Using pagination for large results
```

### Hooks in Action

Hooks run automatically on events:

**Security block (pre-edit):**

```
⛔ BLOCKED: Potential secret detected
   File: src/config.ts, Line 5
   Pattern: API key (sk-...)

   Remove the secret and use environment variables.
```

**Auto-format (post-edit):**

```
✓ Formatted with prettier: src/components/Button.tsx
✓ Formatted with black: scripts/deploy.py
```

**Desktop notifications:**

```
🔔 "Claude needs input" - when waiting for your response
🔔 "Task complete" - when finished
```

---

## Commands Reference

All commands use the format `/project-starter:<command>`.

### Output Styles

| Command                      | Mode                                          |
| -----------------