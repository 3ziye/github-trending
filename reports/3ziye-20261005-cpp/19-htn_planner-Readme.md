# HTN Planner

HTN Planner is a C++ hierarchical task network planner for game AI. Domains are
written in a small declarative language and translated ahead of time into native C.
The runtime executes the generated planner directly and does not parse domain source
during gameplay.

## Project status

HTN Planner is under active development. Published releases are tested, while the
public API, domain language and generated-code ABI continue to evolve.

Before upgrading, review the release notes for compatibility changes and migration
instructions. Some updates require regenerating domains and rebuilding the
integration.

Feedback, bug reports and integration experiences are welcome.

## Overview

The repository includes:

- The generated planner runtime and its C ABI.
- A C++ integration layer with planner hooks and planning units.
- `HTNTranslator`, which validates domains and emits C source.
- A visual SDL and ImGui demo with generated execution debugging.
- An editor, language server, hot reload example, tests and benchmarks.
- Packageable Windows and Linux x64 SDKs with CMake integration.

Version **2.3.0** adds native negative numeric literals such as
`(!remember -1.0 is_moving)`, precise numeric debugger labels and signed-value
diagnostics. Subtraction, negation and decrement remain supported. The C runtime
ABI and atom layout are unchanged from 2.2.0; tools using the C++ compiler AST
must be rebuilt. See the [2.3.0 release notes](docs/RELEASE_2_3_0.md).
For Linux builds, hot reload integration and Windows Natvis distribution, see
the [2.2.0 release notes](docs/RELEASE_2_2_0.md).
For the runtime-list, callterm and generated-code features introduced in 2.1.0,
see its [release notes](docs/RELEASE_2_1_0.md).
Upgrades from older releases must also follow the
[2.0.4 migration guide](docs/RELEASE_2_0_4.md) and, for 2.0.2 or earlier,
the [2.0.3 migration guide](docs/RELEASE_2_0_3.md).

## Domain example

```lisp
(:domain GuardNPC top_level_domain

    (:method (run) top_level_method
        (patrol
            (and
                (guard_on_duty)
            )
            (
                (!move_to "checkpoint")
                (!scan_area)
            )
        )
    )
)
```

A successful decomposition returns a plan containing the primitive tasks
`!move_to` and `!scan_area`. The engine assigns meaning to those tasks and decides
when they start, complete or fail.

## Choosing an integration pattern

See [Planner use cases](docs/USE_CASES.md) for NPC behavior, active-plan validation,
squad coordination and AI Director integration flows. The client owns action
execution, scheduling and cancellation.

## Requirements

### Windows

- Windows x64.
- Visual Studio 2022 with the Desktop development with C++ workload.
- MSVC v143 and a Windows SDK.
- C++20 for clients and C11 for generated domain source.
- CMake 3.25 or newer when consuming the packaged SDK through CMake.

Premake, SDL, Dear ImGui, GoogleTest and the remaining development dependencies are
included in the repository.

### Linux

Ubuntu 24.04 x86_64 is validated with GCC 14 and Clang 18 using libstdc++.
Follow the [Linux build and SDK guide](docs/LINUX.md) for dependency installation,
compilation, tests, visual demos, hot reload and SDK consumers.

```sh
bash BuildAndTestLinux.sh Debug Release Profile ProfileDetailed
bash BuildAndValidateSDK.sh
```

The SDK script rebuilds all four Linux variants and validates external consumers.
It reads `VERSION` unless `--version` is supplied; it does not increment the version
or publish a release. HTNEditor is excluded on Linux while it remains experimental.
See the [validation record](docs/LINUX_SMOKE.md) for scope and evidence.

## Build and run the visual demo

Generate the Visual Studio solution from the repository root:

```bat
GenerateProjectFiles.bat
```

Build `HTN.sln` for x64. Use `Debug` to include generated decomposition capture and
the visual debugger. Use `Release` for an optimized runtime build without debugger
instrumentation.

Run:

```text
bin/<configuration>-windows-x86_64/HTNDemo/HTNDemo.exe
```

The generated-only HTNDemo provides three views:

- **Domain Runner** selects a compiled domain, top-level method, backtracking mode and
  world state. It displays the resulting primitive plan.
- **Generated event debugger** displays the executed hierarchy, backtracking choices,
  source locations, constants and bound variables in instrumented builds.
- **NPC Simulation** runs a generated planner as part of a small agent simulation.

The demo loads world-state data for inspection, but its domain definitions are already
compiled into native generated planners.

## Compiler pipeline

```mermaid
flowchart LR
    Source[".domain source"] --> Lexer["Compiler lexer and tokens"]
    Lexer --> AST["Compiler AST"]
    AST --> Validation["Validation and linking"]
    Validation --> IR["Compiler IR"]
    IR --> Generator["C code generator"]
    Generator --> Native["Native generated planner"]
```

1. `HTNCompiler