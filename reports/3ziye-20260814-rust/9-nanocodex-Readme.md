<div align="center">

<h1>Nanocodex</h1>

<p><strong>Building blocks for frontier OpenAI agents.</strong></p>

[![CI](https://img.shields.io/github/actions/workflow/status/gakonst/nanocodex/ci.yml?branch=master)][ci]
[![Crates.io](https://img.shields.io/crates/v/nanocodex.svg)][crates]
[![Docs.rs](https://img.shields.io/docsrs/nanocodex)][docs]
[![License](https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-blue.svg)][license]

**[Install](#install)** · **[Agent API](#minimal-api-example)** ·
**[Thesis](#thesis)** · **[Components](#components)** ·
**[VM-backed tools](#vm-backed-tools)** ·
**[Evaluation](crates/experimental/nanocodex-eval/README.md)** ·
**[Documentation](#documentation)**

[ci]: https://github.com/gakonst/nanocodex/actions/workflows/ci.yml
[crates]: https://crates.io/crates/nanocodex
[docs]: https://docs.rs/nanocodex
[license]: LICENSE-MIT

</div>

## Install

Install the Nanocodex CLI on macOS or Linux:

```sh
curl -fsSL https://nanocodex.paradigm.xyz | bash
```

Or add the Rust SDK to an application:

```sh
cargo add nanocodex
```

Switch the installed CLI between builds:

```sh
nanocodex update                 # latest stable release
nanocodex update 0.2.0           # exact release, including downgrades
nanocodex update --nightly       # latest nightly
nanocodex update --pr 50         # verified on-demand PR artifact
nanocodex update --path ./nanocodex  # trusted local binary
```

Downloaded builds are retained under `~/.nanocodex/versions`. Running
`nanocodex update 0.2.0` again switches to the cached binary without another
download. A stable launcher keeps `nanocodex update` available even while an
older binary is active, and `~/.nanocodex/current` points to the selected
version.

PR artifacts require an authenticated `gh` CLI and an already completed
on-demand artifact workflow for that PR.

### Interactive cleanup workflow

The TUI includes a behavior-preserving cleanup pass for recently changed code:

```text
/simplify
/simplify focus on memory efficiency
```

The command selects the current Git diff, runs independent reuse,
simplification, efficiency, and abstraction-depth reviewers concurrently, then
deduplicates and applies valid findings. The workflow reuses the CLI's owned
subagent runtime in ordinary TUI sessions. General-purpose subagent tools are
enabled by default and can be disabled with `--subagents false`; the dedicated
cleanup workflow remains available when they are disabled.

## Minimal API Example

```rust,ignore
use nanocodex::{Nanocodex, OpenAi};

let openai = OpenAi::new(std::env::var("OPENAI_API_KEY")?)?;
let (agent, mut events) = Nanocodex::builder(openai)
    .instructions(
        "You are a Rust coding agent. Make focused changes, preserve unrelated work, \
         and run relevant tests before finishing.",
    )
    .workspace(std::env::current_dir()?)
    .build()?;

let event_task = tokio::spawn(async move {
    while let Some(event) = events.recv().await {
        eprintln!("event {}: {:?}", event.seq, event.kind);
        if event.kind.is_terminal() {
            break;
        }
    }
});

// Alternative: stream this turn's response as it arrives:
// use futures_util::StreamExt;
// use nanocodex::agent::events::{AgentEventData, AssistantEvent};
// let mut turn = agent.prompt("Find and fix the failing parser test.").await?;
// while let Some(event) = turn.next().await {
//     if let AgentEventData::Assistant(AssistantEvent::Delta(delta)) = event.data()? {
//         print!("{}", delta.text);
//     }
// }
let result = agent
    .prompt("Find and fix the failing parser test.")
    .await?
    .await?;

event_task.await?;
println!("{}", result.final_message());
```

The first `await` accepts and orders the prompt. The second waits for its typed
`TurnResult`. Follow-on prompts automatically reuse the agent's retained
history, WebSocket, tools, shell sessions, and prompt-cache identity.
`agent.clone()` is a cheap handle to that same session; the independently
returned `AgentEvents` stream is the session-wide event firehose.

Nanocodex supports `gpt-5.6-sol` (the default), `gpt-5.6-terra`, and
`gpt-5.6-luna`. Select a model with `.model(Model::Terra)` or
`.model(Model::Luna)` when creating an agent. The model is fixed for that
thread: switching later would invalidate the provider checkpoint and require
an inefficient replay of the complete retained context.

API-key HTTPS OpenAI routing gateways that namespace model identifiers can set
`NANOCODEX_MODEL_ID_PREFIX`. For example, a prefix of `openai` sends
`openai/gpt-5.6-sol` on the wire while preserving Sol's typed behavior,
pricing, compaction, and snapshot identity inside Nanocodex. This does not add
an alternate provider or arbitrary-model surface.

## Voice: devices or Unix pipes

The non-TUI desktop example owns the default microphone and speaker directly
in Rust, using the same `VoiceSessionBuilder` as the production TUI:

```sh
nanocodex auth login # once; shares ~/.codex/auth.json with Codex
c