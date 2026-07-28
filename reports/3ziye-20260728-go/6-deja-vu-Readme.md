<p align="center"><img src="assets/logo.svg" width="340" alt="deja-vu"></p>

<p align="center"><strong>Your agents already solved this. deja finds it.</strong><br>Memory tools start empty and record forward. deja starts full: it indexes the sessions your coding agents already wrote to disk &mdash; months of history from before you installed it &mdash; searches 3.3&nbsp;GB in ~12&nbsp;ms, serves it back to any agent over MCP, and moves with you between machines over SSH. One zero-dependency binary, fully local.</p>

<p align="center"><strong>84.9% hit@1</strong> on LongMemEval-S retrieval &mdash; no LLM, no embeddings, no API key. <a href="https://vshulcz.github.io/deja-vu/guide/benchmarks.html">Harness in-repo, run it yourself.</a></p>

<p align="center"><a href="https://vshulcz.github.io/deja-vu/">vshulcz.github.io/deja-vu</a> &middot; <a href="https://vshulcz.github.io/deja-vu/guide/compare.html">how deja compares</a></p>

<p align="center">
  <a href="https://github.com/vshulcz/deja-vu/actions/workflows/ci.yml"><img src="https://github.com/vshulcz/deja-vu/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/vshulcz/deja-vu/releases"><img src="https://img.shields.io/github/v/release/vshulcz/deja-vu" alt="Release"></a>
  <a href="https://www.npmjs.com/package/@vshulcz/deja-vu"><img src="https://img.shields.io/npm/v/%40vshulcz%2Fdeja-vu?label=npm" alt="npm"></a>
  <a href="https://scorecard.dev/viewer/?uri=github.com/vshulcz/deja-vu"><img src="https://api.scorecard.dev/projects/github.com/vshulcz/deja-vu/badge" alt="OpenSSF Scorecard"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
</p>

<p align="center"><img src="assets/demo.gif" alt="deja demo"></p>

Claude Code, Codex, opencode, aider, Gemini CLI, Cursor, Antigravity, Grok Build, Qwen Code, Kimi Code, Cline, Roo Code, OpenClaw, Goose, pi and Copilot CLI write every conversation to local files — gigabytes of debugged problems and design decisions you can't search. deja is a zero-dependency binary that turns those histories into a memory layer:

| Feature | What it does |
| --- | --- |
| **Search** | `deja "connection pool exhausted"` — ~12 ms over gigabytes, retroactive: months of logs from before you installed it; natural-language questions fall back to a relevance tier — 84.9% hit@1 on LongMemEval-S session retrieval, harness in-repo; time works too: `deja "what did we do in may"`, "a week ago" |
| **Agent recall** | MCP `recall` tool — the agent answers *"we fixed this three weeks ago"* instead of re-debugging, across harnesses: solve it in Codex, Claude remembers |
| **Sync** | `deja sync ssh laptop` — your memory follows you between machines, append-only, idempotent, no cloud in the middle |
| **Handoff** | `deja handoff --to codex` — stuck in one agent? package the live context and continue in another: `codex "$(deja handoff --to codex)"` |
| **Auto-recall** | `install --auto` adds a SessionStart hook: relevant memory lands in context before you ask — ranked by the files your repo is touching, ~120 ms on a 1000-session index; Claude Code also captures the current transcript before compaction |
| **Déjà vu moments** | When a prompt matches work your history already answered, deja announces it — *you have been here* — with the session and its age, and counts the moment in `deja stats` |
| **Redaction** | API keys, JWTs, private keys are stripped at index time — the cache is safe to keep |
| **View** | `deja view` — your whole memory in one local HTML: sessions, the recall audit trail, curated notes; no server, nothing leaves the machine |
| **Stats** | `deja stats` — your agent work, wrapped; `--impact` reports only counted numbers: recalls served, session starts that began with memory, served-vs-raw ratio |
| **Promote** | `deja promote <id>` — distill a session into a curated note with provenance, `--tag` keywords and a lifecycle state (accepted / rejected / superseded / stale); notes outrank raw transcripts, and promoting over an existing accepted note surfaces the conflict |
| **Trust scopes** | `policy.json` decides what memory activates where: search / MCP / auto × local / imported / per-peer; receipts and `deja log` name the rule |
| **Deep verify** | `deja doctor --deep` proves the index against the sources — re-parses a sample, resolves postings, separates staleness from drift |
| **Share** | `deja share <id>` — hand a colleague a sanitized digest of a session, secrets already scrubbed |
| **Remember** | `deja remember "text"` or MCP `remember` — keep durable decisions and conclusions |
| **Blame** | `deja blame <path>` — which sessions touched this file, what was decided and why |
| **Semantic** | optional: point `deja embed` at a local Ollama/LM Studio and rephrased queries still hit |

## Privacy

`deja forget` removes matching sessions from a rebuilt index and records exact
session tombstones so a later `deja index` cannot restore them from source
his