<h1 align="center">Reverify</h1>

<p align="center">
  <strong>Stop your AI from making things up.</strong><br>
  It proposes; deterministic tools check every claim against ground truth, and only what's verified counts.
</p>

<p align="center">
  <a href="https://pypi.org/project/reverify/"><img src="https://img.shields.io/pypi/v/reverify?color=3fb950" alt="PyPI"></a>
  <img src="https://img.shields.io/pypi/pyversions/reverify" alt="Python">
  <a href="https://github.com/2akouwu/reverify/actions/workflows/ci.yml"><img src="https://github.com/2akouwu/reverify/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://codecov.io/gh/2akouwu/reverify"><img src="https://codecov.io/gh/2akouwu/reverify/graph/badge.svg" alt="Coverage"></a>
  <a href="https://scorecard.dev/viewer/?uri=github.com/2akouwu/reverify"><img src="https://api.scorecard.dev/projects/github.com/2akouwu/reverify/badge" alt="OpenSSF Scorecard"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/2akouwu/reverify" alt="MIT"></a>
  <img src="https://img.shields.io/github/stars/2akouwu/reverify?style=social" alt="Stars">
</p>

<p align="center">
  <a href="https://app.ona.com/#https://github.com/2akouwu/reverify">
    <img src="https://ona.com/build-with-ona.svg" alt="Build with Ona" />
  </a>
</p>

AI is confident and often wrong: it invents an API, a struct field, an offset, or what a
function does, and says it like fact. Reverify makes a deterministic tool the judge — the model
proposes a claim, the tool checks it against the actual artifact, and it comes back **VERIFIED /
REFUTED with evidence**. The model never gets to assert a fact on its own.

Two things it does today:

- **Keeps your AI honest** — every structural or behavioral claim is checked against ground
  truth, not trusted, and only what survives becomes a fact (`reverify verify`, or the MCP
  server your agent already talks to).
- **Keeps your AI's context from rotting** — instead of a lossy auto-summary, `reverify rollover`
  hands the session off to a file and starts a fresh one, so long tasks don't drift or need
  `/clear`. Works in Claude Code, Codex, Gemini CLI and OpenCode.

The hardest place to prove the first point is binary reverse engineering, where hallucination is
worst — so that's where the numbers come from. On 71 real Windows system files the AI's textbook
answer was wrong **97% of the time**; reverify caught every one and **never accepted a wrong
claim** (0 of 71; the same gate runs in CI on Linux and macOS every push, and an independent
aarch64 run found the same) ([EXAMPLE.md](EXAMPLE.md), [BENCHMARK.md](BENCHMARK.md);
`python benchmarks/prologue_prior.py`).

<p align="center">
  <img src="docs/demo.svg" alt="Reverify catches the model's hallucinated prologue on kernel32.dll, then verifies the corrected claim" width="760">
</p>

## The problem

Language models are great at reading code and unreliable at reverse engineering. Ask a
model to reconstruct a struct or an algorithm from a binary and it will confidently invent
offsets, sizes, and behavior. In binary analysis this hallucination problem is far worse
than in source code, and *"did the model just make that up?"* is the single biggest blocker
to using AI for real RE.

## What Reverify does

Reverify pairs a language model with a **deterministic, pure-Python RE toolkit** and makes the
toolkit the judge. The model proposes; the tools verify. A hypothesis about a structure or an
algorithm is only reported once it has been **checked against the actual bytes** — disassembled,
pattern-matched, or executed in the emulator — so the output is grounded in the binary instead
of the model's imagination.

- **Deterministic core** — PE/ELF/Mach-O parsing, x86/x64/ARM/ARM64 disassembly, AOB pattern
  scanning, CPU emulation, Protobuf/TLV dissection, Frida hook generation. Pure Python out of
  the box; installs clean with no Ghidra.
- **Mature engines, optional** — with `pip install "reverify[full]"` the toolkit upgrades
  itself in place to **capstone** (disassembly), **unicorn** (real CPU emulation), **lief**
  (PE/ELF/Mach-O) and **Z3** (proofs); `pip install "reverify[angr]"` adds **angr** for
  function boundaries, the call graph and cross-references. Not installed? It falls back to
  the pure-Python core. `reverify backends` shows what's active.
- **Grounded, not guessed** — structural claims are verified against the binary by the tools.
- **Not only binaries** — `reverify equiv <reference> <candidate> --lang python` (or C) runs a
  candidate implementation and a reference over shared inputs and checks they agree, so an AI's
  rewrite or refactor is *tested, not trusted* — a refutation comes back with the input and both
  outputs. The same rigour, aimed at ordinary source code.
- **Agent-native** — ships as an MCP server, so Claude Code, Cursor, and other agents can call
  the tools directly; also a plain CLI.

> Reverify is for **authorized** reverse engineering — malware analysis, CTF, in