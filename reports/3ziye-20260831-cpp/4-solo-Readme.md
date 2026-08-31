# SoLo — a `.so` loader for static Linux binaries

[![CI](https://github.com/pg83/solo/actions/workflows/ci.yml/badge.svg)](https://github.com/pg83/solo/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/pg83/solo/graph/badge.svg)](https://app.codecov.io/gh/pg83/solo)

**Ship one musl-linked executable. At runtime, load the user's existing
glibc-linked GPU driver. No container, no AppImage, and no second libc in the
process.**

Static binaries are a wonderfully boring way to deploy software on Linux: one
file, no dependencies, nothing to break. We build ours with
[IX](https://github.com/pg83/ix), a source-first build system for producing
fully static Linux binaries. The boredom ends the moment the application needs
the GPU: Vulkan and OpenGL drivers are supplied by the host as shared objects,
usually built against glibc, and a fully static musl binary cannot normally
`dlopen()` them.

SoLo crosses that boundary. It provides a `dlfcn`-style source API backed by
its own ELF loader (x86-64 and aarch64) and a glibc ABI bridge implemented on
top of musl.
The result is still one ordinary static executable, but it can use the graphics
driver already installed on the machine.

The repository includes an end-to-end Vulkan proof: a fully static executable
loads the host's unmodified Vulkan driver, runs a compute shader, and writes
the result to a PNG. Tested on AMD radv, radeonsi, Intel, and NVIDIA GPUs under
Linux, on Apple M1 under Asahi Linux, on Android under Termux, and on WSL with
Mesa's dzn driver over Direct3D 12.

**The host keeps the hardware-specific code. You ship everything else.**

And not on a demo's word alone: on every commit, CI loads the shared
libraries of the 1,000 most-installed Debian packages — over 2,100 host
objects — through SoLo, on both x86-64 and aarch64.

## See it work

Grab the prebuilt binary — no clone, no toolchain, any Linux with a Vulkan
driver installed (`mesa-vulkan-drivers` is enough):

```sh
curl -LO https://github.com/pg83/solo/releases/latest/download/vulkan-x86_64
chmod +x vulkan-x86_64
./vulkan-x86_64 hello.png
```

`vulkan-aarch64` is the same demo for arm64 machines. The command discovers
the distro-installed Vulkan ICD in the usual way and produces a 512×512 RGBA
image. This is how we build the
[Shitty release binaries](https://github.com/pg83/shitty/releases)—a blazingly
fast terminal emulator, BTW! To force a particular driver:

```sh
./vulkan-x86_64 --driver /usr/share/vulkan/icd.d/radeon_icd.x86_64.json radeon.png
./vulkan-x86_64 --driver /usr/share/vulkan/icd.d/lvp_icd.json lavapipe.png
```

ICD manifest names vary slightly between distributions. Passing no `--driver`
lets the embedded Khronos loader perform its normal discovery.

You can verify that the executable itself is not dynamically linked:

```sh
readelf -lW ./vulkan-x86_64 | grep INTERP    # no output
readelf -dW ./vulkan-x86_64                  # "There is no dynamic section"
```

Or build the same demo from source, with Python 3 and a C/C++ compiler in
`PATH`:

```sh
git clone https://github.com/pg83/solo.git
cd solo
./build vulkan
./vulkan hello.png
```

This is not a toy call to `vkCreateInstance`. The demo:

1. enters the statically linked Khronos Vulkan loader;
2. loads the host's Vulkan ICD and its non-glibc dependencies through SoLo;
3. creates a device, storage buffer, descriptor set, and compute pipeline;
4. dispatches a checked-in SPIR-V shader;
5. maps the result and writes it through statically linked libpng.

The complete example is in [`bin/vulkan`](bin/vulkan), and the Vulkan program
itself is in [`main.cpp`](bin/vulkan/main.cpp).

## How it works

```text
┌──────────────────── fully static executable ────────────────────┐
│                                                                 │
│  application → embedded Vulkan loader → SoLo dlopen/dlsym       │
│                                           ├─ x86-64 ELF mapper  │
│                                           └─ glibc ABI → musl   │
│                                           │                     │
└───────────────────────────────────────────┬─────────────────────┘
                                            │ maps at runtime
                                            ▼
                              system Mesa/Vulkan ICD.so + DSOs
```

[`elf_loader.cpp`](lib/elf_loader.cpp) maps ELF segments, walks `DT_NEEDED`,
resolves versioned symbols, applies x86-64 relocations, supports ELF TLS and
TLSDESC, materializes IFUNCs, applies RELRO, and runs initializers. Dependencies
that are themselves ELF DSOs are loaded recursively.

glibc is deliberately *not* loaded. Imports such as `malloc@GLIBC_2.2.5` are
resolved by [`glibc_shim.cpp`](lib/glibc_shim.cpp) to ABI-correct adapters over
the process's existing musl runtime. Unsupported glibc functions have unique
generated stubs that fail loudly with the exact symbol and version if they are
ever called, instead of silently corrupting the process.

Because musl sizes its synchronizatio