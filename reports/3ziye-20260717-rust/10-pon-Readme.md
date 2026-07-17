<p align="center">
  <img src="assets/hero.png" alt="pon — Python, compiled to metal — no interpreter" width="100%" />
</p>

# pon

`pon` is a JIT & AoT native compiler and runtime for Python 3.14, written in Rust. There is no interpreter and no bytecode: every module is parsed with the ruff parser, lowered to one shared IR, and compiled to machine code through Cranelift — either just-in-time inside the process (`pon run`) or ahead-of-time into a standalone native executable (`pon build`). Memory is managed by a Green Tea garbage collector instead of reference counting, and correctness is enforced by a byte-exact differential harness against CPython v3.14.0.

The end goal is the bun/v8 of Python: a runtime that passes the CPython test suite, runs a multi-tier JIT well past CPython, ships single-binary executables, and includes batteries (package manager, tooling) out of the box. The project is under heavy active development — see [Status](#status) for what is true today versus where it is going.

## Quickstart

```sh
# JIT: parse → IR → Cranelift → run, in-process
printf 'def add(a, b):\n    return a + b\n\nprint("hello, world")\nprint(add(2, 3))\n' > hello.py
cargo run -p pon -- run hello.py

# AoT: same IR through cranelift-object, linked into a native executable
cargo run -p pon -- build hello.py -o hello
./hello
```

Both paths print the same bytes CPython would. That property is not aspirational — it is the exit gate of the conformance suite (see [Conformance](#conformance--testing)).

```
pon run <file> [args]
pon build <file> -o <out> [--allow-dynamic] [--opt] [--target <triple>]
pon repl
pon -c 'print(40 + 2)'
pon - < script.py
```

## Architecture

<p align="center">
  <img src="assets/architecture.png" alt="pon workspace architecture" width="100%" />
</p>

One IR, two backends, one runtime ABI. Every tier — baseline JIT, optimizing JIT, and AoT — lowers the same IR and calls the same `pon_*` helper functions:

```
source.py
   │ ruff parser (pinned 0.14.0, PythonVersion::PY314)
AST ──> PON IR (pon-ir, one IR for every tier)
   │
   ├── pon run:   pon-codegen ──> cranelift-jit ──> native code in process
   │                 tier-0 baseline (all boxed)
   │                 tier-1 typed: inline caches, OSR, background compile
   │
   └── pon build: pon-codegen ──> cranelift-object ──> object file ──> linked executable
   │
pon-runtime  (object model, builtins, NULL-sentinel pon_* ABI)
pon-gc       (Green Tea garbage collector)
```

**Object model:** CPython's heap object layout minus the refcount header. Errors cross the ABI as NULL sentinels, not unwinding. Integers are arbitrary-precision (`num-bigint` behind `PyLong`); a tagged small-int fast path is landing in the typed tier.

**Tiering:** tier-0 compiles everything boxed with no type feedback and is the correctness baseline (`PON_TIER0_ONLY=1` forces it). Runtime helpers feed `FeedbackCell` type profiles from the first execution; hot functions recompile on a background thread and running loops enter the optimized code via on-stack replacement.

**GC:** the Green Tea collector owns all Python objects. Tier-0 uses conservative stack scanning with a register-flush trampoline at safepoints; the typed tier upgrades to precise Cranelift user stack maps.

## Workspace

| Crate | Role |
| --- | --- |
| `pon-ir` | ruff-based frontend: parse Python 3.14, lower to the shared PON IR |
| `pon-codegen` | IR → Cranelift CLIF, shared by every backend and tier |
| `pon-jit` | in-process compilation, tiering, inline caches, OSR, background compile |
| `pon-aot` | `cranelift-object` backend: object files and linked native executables |
| `pon-runtime` | object model, builtins, stdlib native modules, the `pon_*` helper ABI |
| `pon-gc` | Green Tea garbage collector |
| `pon-abi` | ABI types shared between codegen and runtime |
| `pon` | the `pon` binary: `run`/`build`/`repl` entry points + package manager (index client, resolver, wheel/sdist install) |
| `pon-conformance` | differential conformance suites, fuzzing, benchmarks, floor ratchets |

All dependencies are declared once in the root `Cargo.toml` under `[workspace.dependencies]`; member crates only inherit (see [`AGENTS.md`](AGENTS.md)).

## Conformance & testing

The correctness contract is differential: a corpus module passes only if `pon` produces **byte-identical output** to CPython v3.14.0 (`TZ=UTC`, `PYTHONHASHSEED=0`). Passing sets are ratcheted into committed floor files, and CI fails on any regression below the floor.

| Suite | What it measures | Committed floor |
| --- | --- | --- |
| `cpython` | corpus modules, JIT, byte-exact vs CPython 3.14 | 244 modules ([`conformance-floor.json`](conformance-floor.json)) |
| `cpython-aot-subset` | same corpus compiled AoT and executed as native binaries | 206 modules ([`aot-parity-floor.json`](aot-parity-floor.json)) |
| `cpython-full` | CPython's own test suite (`Lib/test`), run under pon | being brought up ([`conformance-full-floor.json`](conformance-full-f