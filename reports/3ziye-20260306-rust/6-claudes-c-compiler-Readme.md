# CCC — Claude's C Compiler

A C compiler written entirely from scratch in Rust, targeting x86-64, i686,
AArch64, and RISC-V 64. Zero compiler-specific dependencies — the frontend,
SSA-based IR, optimizer, code generator, peephole optimizers, assembler,
linker, and DWARF debug info generation are all implemented from scratch.
Claude's C Compiler produces ELF executables without any external toolchain.

> Note: With the exception of this one paragraph that was written by a human, 100% of the code and documentation in this repository was written by Claude Opus 4.6. A human guided some of this process by writing test cases that Claude was told to pass, but never interactively pair-programmed with Claude to debug or to provide feedback on code quality. As a result, I do not recommend you use this code! None of it has been validated for correctness. Claude wrote this exclusively on a Linux host; it probably will not work on MacOS/Windows — neither I nor Claude have tried. The docs may be wrong and make claims that are false. See [our blog post](https://anthropic.com/engineering/building-c-compiler) for more detail.

## Prerequisites

- **Rust** (stable, 2021 edition) — install via [rustup](https://rustup.rs/)
- **Linux host** — the compiler targets Linux ELF executables and relies on
  Linux system headers / C runtime libraries (glibc or musl) being installed
  on the host
- For cross-compilation targets (ARM, RISC-V, i686), the corresponding
  cross-compilation sysroots should be installed (e.g.,
  `aarch64-linux-gnu-gcc`, `riscv64-linux-gnu-gcc`)

## Building

```bash
cargo build --release
```

This produces five binaries in `target/release/`, all compiled from the same
source. The target architecture is selected by the binary name at runtime:

| Binary | Target |
|--------|--------|
| `ccc` | x86-64 (default) |
| `ccc-x86` | x86-64 |
| `ccc-arm` | AArch64 |
| `ccc-riscv` | RISC-V 64 |
| `ccc-i686` | i686 (32-bit x86) |

## Quick Start

Compile and run a simple C program:

```bash
# Write a test program
cat > hello.c << 'EOF'
#include <stdio.h>
int main(void) {
    printf("Hello from CCC!\n");
    return 0;
}
EOF

# Compile and run (x86-64)
./target/release/ccc -o hello hello.c
./hello

# Cross-compile for AArch64 and run under QEMU
./target/release/ccc-arm -o hello-arm hello.c
qemu-aarch64 -L /usr/aarch64-linux-gnu ./hello-arm
```

CCC works as a drop-in GCC replacement. Point your build system at it:

```bash
# Build a project with make
make CC=/path/to/ccc-x86

# Build a project with CMake
cmake -DCMAKE_C_COMPILER=/path/to/ccc-x86 ..

# Build a project with configure scripts
./configure CC=/path/to/ccc-x86
```

## Usage

```bash
# Compile and link
ccc -o output input.c                # x86-64
ccc-arm -o output input.c            # AArch64
ccc-riscv -o output input.c          # RISC-V 64
ccc-i686 -o output input.c           # i686

# GCC-compatible flags
ccc -S input.c                       # Emit assembly
ccc -c input.c                       # Compile to object file
ccc -E input.c                       # Preprocess only
ccc -O2 -o output input.c            # Optimize (accepts -O0 through -O3, -Os, -Oz)
ccc -g -o output input.c             # DWARF debug info
ccc -DFOO=1 -Iinclude/ input.c       # Define macros, add include paths
ccc -Werror -Wall input.c            # Warning control
ccc -fPIC -shared -o lib.so lib.c    # Position-independent code
ccc -x c -E -                        # Read from stdin

# Build system integration (reports as GCC 14.2.0 for compatibility)
ccc -dumpmachine     # x86_64-linux-gnu / aarch64-linux-gnu / riscv64-linux-gnu / i686-linux-gnu
ccc -dumpversion     # 14
```

The compiler accepts most GCC flags. Unrecognized flags (e.g., architecture-
specific `-m` flags, unknown `-f` flags) are silently ignored so `ccc` can
serve as a drop-in GCC replacement in build systems.

### Assembler and Linker Modes

By default, the compiler uses its **builtin assembler and linker** for all
four architectures. No external toolchain is required. You can verify this
with `--version`, which shows `Backend: standalone` when using the builtin
tools.

To build with optional GCC fallback support (e.g., for debugging), enable
Cargo features at compile time:

```bash
# Build with GCC assembler and linker fallback
cargo build --release --features gcc_assembler,gcc_linker

# Build with GCC fallback for -m16 boot code only
cargo build --release --features gcc_m16
```

| Feature | Description |
|---------|-------------|
| `gcc_assembler` | Use GCC as the assembler instead of the builtin |
| `gcc_linker` | Use GCC as the linker instead of the builtin |
| `gcc_m16` | Use GCC for `-m16` (16-bit real mode boot code) |

When compiled with GCC fallback features enabled, `--version` shows which
components use GCC (e.g., `Backend: gcc_assembler, gcc_linker`).

## Status

The compiler can build real-world C codebases across all four architectures,
including the Linux kernel. Projects that compile and pass their test su