# scfw

A cross-platform C++ framework for building Windows shellcode.
Supports Linux, macOS, or Windows development environments.
Creates position-independent blob that runs in user-mode or kernel-mode, x86 or x64.

```cpp
#include <scfw/runtime.h>
#include <scfw/platform/windows/usermode.h>

IMPORT_BEGIN();
    IMPORT_MODULE("kernel32.dll");
        IMPORT_SYMBOL(WriteConsoleA);
IMPORT_END();

namespace sc {

extern "C" void __fastcall entry(void* argument1, void* argument2)
{
    HANDLE StdOut = NtCurrentPeb()->ProcessParameters->StandardOutput;
    WriteConsoleA(StdOut, _T("Hello, World!\n"), 14, NULL, NULL);
}

} // namespace sc
```

Build it, extract the `.text` section, and you have a self-contained shellcode binary that resolves its own imports at runtime.

## Motivation

As with all my projects, it boils down to _"I need that, current solutions were unsatisfactory, and I want to learn something"_.

I like to experiment with <abbr title="Virtual Machine Introspection">VMI</abbr> and sometimes it's really useful to be able to inject a piece of code into the memory of some process (and/or kernel) and execute it. And because [`vmi-rs`](https://github.com/vmi-rs/vmi) development happens on Linux, and my daily driver became macOS, I wanted a convenient way to generate Windows shellcode on them.

Although compression and "non-null" shellcode are not the primary goals of this project, they might be interesting additions in the future.

## Table of Contents

- [Motivation](#motivation)
- [Installation](#installation)
- [Building](#building)
- [Running Shellcode](#running-shellcode)
- [Architecture](#architecture)
  - [The Dispatch Table](#the-dispatch-table)
  - [Section Layout](#section-layout)
  - [Position-Independent Code](#position-independent-code)
- [User-Mode Shellcode](#user-mode-shellcode)
- [Kernel-Mode Shellcode](#kernel-mode-shellcode)
- [Compile-Time Options](#compile-time-options)
- [Per-Entry Flags](#per-entry-flags)
- [CMake Build Options](#cmake-build-options)
- [Examples](#examples)
- [License](#license)

## Installation

### Prerequisites

_scfw_ cross-compiles Windows shellcode from any host OS. You don't need a Windows machine to build.

- **CMake** 3.22+
- **Ninja** build system
- **clang** clang 19+
  - _**Note:**_ On Windows, [clang 21+ currently experiences issues with `/FILEALIGN:1` during linking](https://github.com/llvm/llvm-project/issues/180406).
    If you encounter linker errors, try to compile with `-DSCFW_FILE_ALIGNMENT=0` or switch to older clang version.
- **LLVM tools**: `lld-link`, `llvm-objcopy`, `llvm-readobj`
- **Windows SDK** headers and libraries (can be fetched automatically on any platform, see below)

### Dependencies

**[phnt](https://github.com/winsiderss/phnt)** (Windows native API headers) is fetched automatically by CMake via `FetchContent`. No action needed.

**Windows SDK** is the only dependency that requires some setup, especially on non-Windows hosts. On Windows with MSVC, CMake detects the system SDK automatically. On macOS and Linux (or Windows without the SDK), CMake will tell you it's missing and suggest how to fetch it.

The easiest option is to let CMake download it for you:

```bash
cmake --preset x64 -DSCFW_FETCH_WINSDK=ON
```

This runs `scripts/fetch-winsdk.sh` (or `fetch-winsdk.ps1` on Windows), which uses [xwin](https://github.com/Jake-Shadle/xwin) to download the Windows SDK. If `xwin` isn't installed, the script looks for Rust toolchain and installs `xwin` via `cargo install`. If Rust isn't installed either, the script downloads a temporary Rust toolchain, installs `xwin`, downloads the SDK, and then cleans up both the Rust toolchain and `xwin`. Nothing is left behind on your system - the temporary installations are fully isolated.

Alternatively, you can manually place the Windows SDK into the `winsdk/` directory at the project root. The expected structure is:

```
winsdk/
  crt/
    include/
    lib/{x86,x86_64}/
  sdk/
    include/{ucrt,um,shared}/
    lib/{um,ucrt}/{x86,x86_64}/
```

## Building

The project uses CMake presets for convenience:

```bash
# x64 Release
cmake --preset x64
cmake --build build-x64

# x86 Release
cmake --preset x86
cmake --build build-x86
```

Debug builds are also available (`x64-debug`, `x86-debug`), but shellcode extraction is disabled in Debug mode. You get a PE executable for debugging instead.

After building, each example produces both a `.exe` and a `.bin` (the extracted shellcode).

## Running Shellcode

The `scrun` tool loads a shellcode binary into executable memory and runs it. It's built alongside the examples and requires Windows to run.

```
.\build-x64\tools\scrun.exe .\build-x64\examples\writeconsole\writeconsole.bin
.\build-x64\tools\scrun.exe .\build-x64\examples\opengl_triangle\opengl_triangle.bin
.\build-x86\tools\scrun.exe .\build-x86\examples\messagebox\messagebox.bin
```

`scrun` accepts two optional arguments that are passed to the shellcode via the first and second parameters (RCX/