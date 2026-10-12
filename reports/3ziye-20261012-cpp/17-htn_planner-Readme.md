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

Version **2.4.0** is being prepared. Domains use `0`/`1` for boolean matching;
bare `true`/`false` are ordinary symbols. The debugger and natvis display BOOL
as `0`/`1`. Migrate old boolean literals and regenerate domains. Standalone
callterm conditions continue to require a BOOL result.

Optional per-instance allocators now control owning lists and backtracking
overflow. List pools can use a safe new/delete fallback; backtracking supports
client-owned scratch memory and per-call usage statistics. See the
[list allocator](docs/INSTANCE_LIST_ALLOCATOR.md) and
[backtracking allocator](docs/BACKTRACKING_ALLOCATOR.md) lifetime contracts.

**ABI migration:** regenerate domains and rebuild the host and runtime bridge
with matching headers and libraries. Previous generated modules are rejected.

Instrumented builds retain facts that the
domain does not reference in `HTNWorldState::GetUnregisteredFacts()` for inspection.
Those writes still return `false`, and the planner cannot query the captured rows.
Plain builds retain their previous behavior. The instrumented C++ world-state
layout also changes. Atom/list layouts remain unchanged. See the
[2.4.0 release notes](docs/RELEASE_2_4_0.md).

Native negative literals, numeric debugger labels and their compiler-tool migration
requirements are documented in the [2.3.0 release notes](docs/RELEASE_2_3_0.md).
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