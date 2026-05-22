# statewright

> Agents are suggestions, states are laws.

State machine guardrails that control which tools your AI agent can use in each phase. Define a workflow once, enforce it across Claude Code, Codex, Cursor, opencode, and Pi. [Full docs →](https://docs.statewright.ai)

![Statewright workflow editor](docs/images/workflow-editor.png)

## The problem

AI agents are brittle. Give a model 40+ tools and an open-ended problem and it re-reads the same file five times, calls Edit during review, deploys before tests pass. The common fix is bigger models and longer prompts... it helps sometimes. Observability tells you what went wrong after the fact; it doesn't prevent it.

## The approach

Instead of making the model bigger, make the problem smaller.

State machines constrain the tool and solution spaces so the model reasons in a focused context at each step. A planning state gets read-only tools. When the agent transitions to implementation, edit tools unlock with limited shell access. Write-via-redirect and destructive ops are still blocked even when Bash is allowed. Testing only permits designated test commands.

Call a tool that's not in the current phase and you get rejected with a message telling you what IS available and how to transition. State machines loop and retry (unlike DAGs), which is what agentic work actually needs.

Works on frontier and local models alike. Below 13GB, models can produce tool calls but can't retain enough file content to make accurate edits. Above that threshold, the guardrails start turning failures into completions.

## Quickstart

Install into Claude Code:

```
/plugin marketplace add statewright/statewright
/plugin install statewright
```

Your browser opens → sign up at [statewright.ai](https://statewright.ai) → generate a key → paste it → done.

Then start a workflow:

```
❯ start the bugfix workflow — fix the failing tests in calc.py

◆ statewright — statewright_start (workflow: bugfix)
◆ [statewright] Workflow activated: bugfix

◆ statewright — statewright_get_state (MCP)

◆ Current phase: planning. Let me read the code first.

  Read 2 files

  [statewright] planning => implementing

◆ statewright — statewright_transition (READY)

  Edit calc.py: 1 line changed

  [statewright] implementing => testing

◆ statewright — statewright_transition (DONE)

  Bash: pytest -x — 7 passed

  [statewright] testing => completed
◆ [statewright] Workflow complete. 46 seconds.
```

You can also use the slash command directly: `/statewright start bugfix`.

## Research results

In our 5-task SWE-bench subset (not the full 2294-instance benchmark), two local models **went from 2 of 10 attempts passing to 10 of 10** with statewright constraints. Same tasks, same hardware.

| Model | Size | Bug Fix (26 lines) | SWE-bench (5 tasks) |
|-------|------|--------------------|---------------------|
| gemma3 | 3.3GB | FAIL | FAIL |
| gemma4:e2b | 7.2GB | PASS* | FAIL |
| gpt-oss:20b | 13.8GB | PASS | PASS (5/5) |
| gemma4:31b | 19.9GB | PASS | PASS (5/5) |
| llama3.3 | 42.5GB | PASS | PASS (2/2)† |

*\*with specialized edit_line tool adaptation*
*†tested on 2 of the 5 tasks (added after initial experiment run)*

The floor is around 13GB. Below that, models identify bugs correctly but can't serialize surgical edits (they rewrite entire files). That's a model limitation, not ours.

The structural win on larger models is breaking read-loop death spirals and keeping the tool space small enough that the model reasons instead of flailing. [Research brief →](https://statewright.ai/research)

## How it works

The core is a Rust engine that evaluates state machine definitions: states, transitions, guards, tool restrictions. It's deterministic. No LLM in the loop.

On top of that sits a plugin layer that integrates with your coding agent via MCP. When you activate a workflow, hooks enforce tool restrictions per state. The model sees 5 tools instead of 30. It gets clear instructions for the current phase and transitions when conditions are met.

### Guardrails

| Guardrail | What it does |
|-----------|-------------|
| Per-state tool enforcement | Agent can't see or call tools outside `allowed_tools` for the current state |
| Bash discernment | Blocks `echo > file`, `rm -rf`, `sed -i`, and scripting interpreters (`python`, `node`) when Write/Edit aren't allowed. Even if Bash itself is permitted. |
| Edit guards | Rejects diffs exceeding `max_edit_lines`, caps files edited per state |
| Command allow-lists | Only prefix-matched commands run (e.g. `pytest`, `cargo test`) |
| Conditional transitions | Programmatic guards on context data: `test_result eq pass`, `coverage gt 80` |
| Approval gates | `requires_approval` pauses for human review |
| Interrupts | Edit a file matching a glob pattern? Auto-transition to a validation state, then return where you were |
| Fork/join | Run branches sequentially or in parallel, join when all (or any) complete |
| Environment scoping | Hide `PROD_DB_URL` via `blocked_env`,