<p align="center">
  <a href="https://turaai.net/">
    <img src="assets/tura/icon.svg" alt="Tura icon" width="96">
  </a>
</p>

<p align="center">
  <a href="https://turaai.net/"><img alt="Website" title="Tura official website" src="https://img.shields.io/badge/Website-turaai.net-40e0d0?style=flat-square&amp;labelColor=555555"></a>
  <a href="https://turaai.net/benchmark"><img alt="Benchmark: 348 sessions" title="Tura benchmark: 348 sessions" src="https://img.shields.io/badge/Benchmark-348_sessions-9b59b6?style=flat-square&amp;labelColor=555555"></a>
  <a href="https://www.npmjs.com/package/tura-ai"><img alt="npm package" title="Tura npm package" src="https://img.shields.io/npm/v/tura-ai?style=flat-square&amp;logo=npm&amp;label=npm&amp;labelColor=555555&amp;color=cb3837"></a>
</p>

<p align="center"><strong>English</strong> | <a href="README.zh-CN.md">简体中文</a></p>

<h1 align="center">Tura: 83.1% fewer turns; 16.7 percentage points higher success.</h1>

Tura is a local, open-source coding agent for developers who are tired of vague skill claims, token-saving extensions with no evidence, and agents without judgment wreck their repos.

Across 20 DeepSWE v1.1 tasks, tested 60 sessions with GPT-5.6 SOL at High reasoning effort, Tura creates a substantial token-budget advantage by reducing repeated context and model round trips. You can spend that advantage in two ways. Direct turns most of it into lower cost: 83.5% fewer aggregate tokens than the official Codex CLI High configuration, with a verifier success rate of 65.0% versus 60.0%. Balanced puts more of the saved budget back into reasoning, investigation, and verification. It reached an 80.0% success rate—20 percentage points higher than Codex CLI High—while still using 49.6% fewer tokens.[^test-set-record][^debug-manifests]

### Benchmark

Long-horizon task [benchmarks](https://turaai.net/benchmark) are one way to look past a polished isolated prompt and see how an agent handles real work. The published comparison uses harness-based development tasks with archived prompts, per-round tool calls, token usage, patches, and verifier results.

> The primary comparison below holds the model and reasoning label fixed: Tura Balanced High, Tura Direct High, and the official Codex CLI High configuration on 20 DeepSWE tasks and 5 rewrite tasks. The evidence record also retains Codex CLI Medium as a separate secondary configuration; the benchmark methodology keeps 2 separately reviewed design tasks outside the harness-scored population.[^test-set-record]

[Full report on GitHub](https://github.com/Tura-AI/benchmark/blob/main/doc/current-test-set-record.md)

The published results do not establish equivalent quality or performance for
every configured provider. Broader Anthropic/Claude, Google/Gemini,
OpenAI-compatible, local-provider, UI-latency, runtime/session parsing, and
cross-OS measurements remain part of the documented
[roadmap](ROADMAP.md) and [known evidence gaps](docs/KNOWN_ISSUES.md).

<details>
<summary><strong>FULL BENCHMARK REPORT</strong></summary>

<img src="assets/data/benchmark-agent-comparison.svg" alt="High-to-High benchmark comparison" width="800">
</details>

### Screenshots

<p align="center">
  <img src="assets/screenshot/gui-ci-quality-demo.svg" alt="Tura GUI" width="800">
</p>

<p align="center"><em>GUI page with multi-session concurrent work and HTML rich text support.</em></p>

<p align="center">
  <img src="assets/screenshot/tui-ci-quality-demo.svg" alt="Tura TUI" width="800">
</p>

<p align="center"><em>TUI page with multi-session concurrent work and HTML rich text support.</em></p>

The results below come from published benchmark artifacts, not an uncited aggregate. Three systems do most of the work:

## Macro CLI Command Run

Most coding agents still depend on repetitive tool-calling loops: inspect, wait, patch, wait, build, wait, test, wait.

_**Tool-calling coding agent:**_

```bash
# Turn 1 — inspect environment

rg -n "TODO|command_run|handler" crates/
rg --files crates/runtime/src crates/tools/src
```

```bash
# Turn 2 — apply patch

*** Begin Patch
*** Update File: crates/tools/src/command_run/handler.rs
@@
-    // old command handler logic
+    // patched command handler logic
*** End Patch
```

```bash
# Turn 3 — build

cargo build -p runtime
```

```bash
# Turn 4 — run tests

cargo test -p runtime --lib
```

```bash
# Turn 5 — run lint validation

cargo clippy -p runtime --all-targets
```

Tura takes a different route. Instead of exposing dozens of small tools to the model, it exposes one macro tool: `command_run`. The agent can then build a multi-step execution tree and run related actions in one LLM turn.

In the example below, both agents run the same commands. A normal tool-calling agent needs five LLM turns; Tura handles the sequence as one structured macro workflow. The saved work is conversational overhead, not engineering discipline.

_**Tura macro CLI command:**_

```json
{
  "name": "command_run",
  "arguments": {
    