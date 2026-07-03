<div align="center">
  <img src="./assets/headbar.png" alt="Loom" width="100%">
  <p><strong>Loop engineering for agentic software delivery.</strong></p>
  <p>An open delivery harness that turns Claude Code, Codex, OpenCode and other coding agents into repeatable software delivery systems.</p>
  <p>
    <a href="./README.zh-CN.md">Simplified Chinese</a>
    ·
    <a href="https://zonodqioyxil6r3k.public.blob.vercel-storage.com/Loomline-v0.pdf">Technical Report</a>
    ·
    <a href="./docs/use-cases.md">Use Cases</a>
    ·
    <a href="#quick-start">Quick Start</a>
    ·
    <a href="#how-to-use">How to Use</a>
    ·
    <a href="#token-saving-context">Token Saving</a>
    ·
    <a href="#faq">FAQ</a>
  </p>
  <p>
    <a href="./LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/badge/License-Apache--2.0-blue.svg"></a>
    <a href="https://discord.gg/Yr7UjwbYPC"><img alt="Discord" src="https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&logoColor=white"></a>
    <img alt="Rust" src="https://img.shields.io/badge/Rust-MCP%20runtime-b7410e?logo=rust&logoColor=white">
    <img alt="Python" src="https://img.shields.io/badge/Python-algorithms-3776AB?logo=python&logoColor=white">
    <img alt="Status" src="https://img.shields.io/badge/status-open-brightgreen">
  </p>
</div>

## What Is Loom?

Loom is an open-source delivery harness for existing coding agents. It does not replace the model or editor you already use; it turns each delivery goal into a structured loop of planning, building, verification, repair, preview, and handoff.

Loom uses dynamic workflows to choose the right delivery path for each goal, then makes that path durable: project context, task contracts, backend state, test results, preview evidence, repair notes, and handoff reports are persisted so the next session or agent can continue without starting over.

Instead of a one-shot prompt chain, Loom treats delivery as a loop: route the next step, execute, verify, record evidence, repair when needed, and continue from saved state.

Coding agents can write code. Loom helps them keep the delivery promise from idea to release, with fewer wasted tokens.

Use Loom when a request is larger than a one-shot edit: a feature needs clarification, architecture, task splitting, implementation evidence, review, repair, preview, deployment, or a clean handoff.

## Why a Harness?

Website and app generation is becoming table stakes. The harder problem is reliable delivery: keeping the agent aligned after compaction, preserving requirements across many turns, verifying its own work without bias, repairing failures, and resuming from the right step after an interruption.

Long-running agent work tends to break down in predictable ways:

Failure mode | Loom response
--- | ---
Partial completion | Bounded tasks, explicit result files, continue routing, and final-response guards keep agents from declaring done after partial progress.
Goal drift | Confirmed scope, architecture contracts, task plans, and compact context packs preserve the original objective across sessions.
Self-check bias | Review, verification, repair requests, and evidence records separate implementation from validation.
Token waste | Project summaries, task graphs, backend/runtime state, test results, and deployment evidence reduce repeated whole-repo reads.
Handoff gaps | Delivery reports, preview checks, logs, and repair history make the final state inspectable by humans and other agents.

The hard part is the harness around the model: durable state, scoped work, routing, verification, recovery, and human-readable evidence. Loom uses dynamic workflows as the operating pattern, then lifts them to the project level so delivery can survive interruptions, compaction, agent switches, and future handoffs.

That is where Loom is different from prompt files, one-off workflows, and single-agent scripts: it stores delivery state in `.loom/`, exposes an MCP tool protocol to coding agents, and makes verification, repair, preview, and handoff first-class protocol steps.

## From Demo to Delivery

Vibe Coding and AI Coding are making software creation accessible to more builders than ever. More people can now turn an idea into a demo, prototype a product, or build a tool for themselves with the help of coding agents.

But there is still a large gap between a demo that works once and a production-grade application that can be trusted, shipped, repaired, and evolved.

That gap is not only about model capability. Even as models improve, builders still need to clarify requirements, preserve project context, make architectural decisions, prepare backend/runtime state, run checks, inspect failures, repair issues, verify again, preview the result, and collect delivery evidence.

Loom exists to close that gap.

It is an open-source delivery layer for existing coding agents. It helps agents move from one-shot coding to repeatable software delivery: clarify the request, plan the work, split tas