# sepia

**English** | [繁體中文](README.zh-TW.md) | [简体中文](README.zh-CN.md)

[![behavioral eval](https://github.com/Nanako0129/sepia/actions/workflows/behavioral-eval.yml/badge.svg)](https://github.com/Nanako0129/sepia/actions/workflows/behavioral-eval.yml) [![version consistency](https://github.com/Nanako0129/sepia/actions/workflows/version-consistency.yml/badge.svg)](https://github.com/Nanako0129/sepia/actions/workflows/version-consistency.yml) [![release](https://img.shields.io/github/v/release/Nanako0129/sepia)](https://github.com/Nanako0129/sepia/releases/latest) [![license: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> De-AI writing at the layer that actually gives AI away. Fiction gets its narrative architecture repaired before anyone touches word choice; professional documents (release notes, PR replies, postmortems, tickets, technical articles) each get rules matched to their venue.

A portable [Agent Skill](https://agentskills.io/specification): any agent that speaks the standard can load it, and the [Skills CLI](https://skills.sh), which supports 77+ agents, installs it with one command. Claude Code, Codex, Grok Build, and Antigravity additionally get native plugin packaging. One canonical `SKILL.md`, no per-platform forks. Four operations: **write**, **review** (diagnose only), **refactor** (minimal edits), **recreate** (full rewrite).

## Why another humanizer

Every popular humanizer edits word choice and syntax. [StoryScope](https://arxiv.org/abs/2604.03136) (Russell et al., 2026: 61,608 stories, human + 5 frontier LLMs) showed that a classifier using **narrative-structure features alone** detects AI fiction at 93.2% macro-F1. In the same study's LAMP-edited condition, where human editors had rewritten the surface style, detection dropped only from 95.5% to 93.9%. The tells that survive are architectural: themes explained by the narrator, single-track causally-tidy plots, emotions rendered only as bodily sensation, no real-world references, no reader, linear time, endings resolved by protagonist growth and acceptance.

sepia turns those measured gaps, together with the related studies digested in [`research/`](research/), into a three-pass writing and revision protocol for fiction:

| Pass | Layer | Examples |
|---|---|---|
| 1 | Narrative architecture (fiction) | stop explaining the theme, loosen the causal chain, back-load revelations, mix emotion modes, sparse character networks, name real things |
| 2 | Discourse flow | de-template the paragraph-question sequence, fix the mid-story sag, vary rhythm and positions |
| 3 | Surface style | the classic layer: clichés, syntax templates, vocabulary, register |

Plus a 30-feature diagnosis rubric and per-model fingerprints in two layers: narrative tells measured by StoryScope (Claude, GPT, Gemini, DeepSeek, Kimi) and sentence-level tells taken from the vendors' own prompting guides (Claude Fable 5.1 and Mythos 5.1, Fable 5 and Mythos 5, Opus 5, Opus 4.8; GPT-5.6; Gemini 3 series), applied when the writing or executing model is known. Vendors that publish no such guidance are recorded as consulted, not guessed.

Professional prose fails differently. The studies digested in [`research/`](research/) point at filler that carries no information, hedging where a judgment was needed, chatbot leftovers, register that ignores the venue, and formatting that looks stamped out. Each document type gets a thin rule file on top of one shared checklist:

| Domain | The gist |
|---|---|
| Release notes / announcements | user impact first, artifacts per claim, no marketing inflation |
| PR / issue replies | answer first, cite `file:line`, no reflex praise, length ∝ stakes |
| Postmortems | blameless toward people, merciless toward mechanisms; timestamps, dead ends, owned action items |
| Tickets / work orders | title = outcome, testable acceptance criteria, link don't repeat |
| Technical articles | open at the problem, one real dead end, one committed opinion, numbers with conditions |

The governing principle throughout: **calibrate to the human distribution, don't invert the AI one.** Humans sit at moderate values; a story with every rule applied is a new fingerprint. The skill selects 3–5 moves per story and leaves slack.

## Operation entries

The complete plugin package gives Claude Code, Codex, Grok Build, and Antigravity a general router plus five direct entries:

| Operation | Claude Code | Codex | Grok Build | Antigravity | Meaning |
|---|---|---|---|---|---|
| write | `/sepia-write` | `$sepia-write` | `/sepia-write` | `/sepia-write` | Create new prose |
| review | `/sepia-review` | `$sepia-review` | `/sepia-review` | `/sepia-review` | Diagnose without editing |
| refactor | `/sepia-refactor` | `$sepia-refactor` | `/sepia-refactor` | `/sepia-refactor` | Make minimal in-place edits |
| recreate | `/sepia-recreate` | `$sepia-recreate` | `/sepia-recreate` | `/sepia-recreate` | Rewrite from the source facts and intent |
| hemingway | `/se