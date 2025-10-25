# OpenZL

OpenZL delivers high compression ratios _while preserving high speed_, a level of performance that is out of reach for generic compressors. **Check out the [blog post](https://engineering.fb.com/2025/10/06/developer-tools/openzl-open-source-format-aware-compression-framework/) and [whitepaper](https://arxiv.org/abs/2510.03203) for a breakdown of how it works.**

OpenZL takes a description of your data and builds from it a specialized compressor optimized for your specific format. [Learn how it works →](https://facebook.github.io/openzl/getting-started/introduction/)

OpenZL consists of a core library and tools to generate specialized compressors —
all compatible with a single universal decompressor.
It is designed for engineers that deal with large quantities of specialized datasets (like AI workloads for example) and require high speed for their processing pipelines.

See our [docs](https://facebook.github.io/openzl) for more information and our [quickstart guide](https://facebook.github.io/openzl/getting-started/quick-start) to get started with a guided tutorial.

## Project Status

This project is under active development. The API, the compressed format, and the set of codecs and graphs included in OpenZL are all subject to (and will!) change as the project matures.

However, we intend to maintain some stability guarantees in the face of that evolution. In particular, payloads compressed with any release-tagged version of the library will remain decompressible by new releases of the library for at least the next several years. And new releases of the library will be able to generate frames compatible with at least the previous release.

(Commits on the `dev` branch offer no guarantees whatsoever. Use only release-tagged commits for any non-experimental deployments.)

Despite the big scary warnings above, we consider the core to have reached production-readiness, and OpenZL is used extensively in production at Meta.

## Building OpenZL

### Prerequisites
OpenZL requires a compiler that supports C11 and C++17. When building with `cmake`, `cmake 3.20.2` or newer is required. There is ongoing work to relax these restrictions. As that happens, this section will be updated.

### Build with `make`

The OpenZL library and essential tools can be built using `make`:

```sh
make
```

#### Build Options

The `Makefile` supports all standard build variables, such as `CC`, `CFLAGS`, `CPPFLAGS`, `LDFLAGS`, `LDLIBS`, etc.

It builds with multi-threading by default, auto-detecting the local number of cores, and can be overridden using standard `-j#` flag (ex: `make -j8`).

#### Build Types

Binary generation can be altered by explicitly requesting a build type:

Example:
```sh
make lib BUILD_TYPE=DEV
```

Build types are documented in `make help`, and their exact flags are detailed with `make show-config`.

Usual ones are:

* `BUILD_TYPE=DEV`: debug build with asserts enabled and ASAN / UBSAN enabled
* `BUILD_TYPE=OPT`: optimized build with asserts disabled (default)

### Build with `cmake`

OpenZL can be built using `cmake`. Basic usage is as follows:

```sh
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release -DOPENZL_BUILD_TESTS=ON ..
make -j
make -j test
```

Details on setting CMake variables is below.

#### Build Modes

By default, we ship several different predefined build modes which can be set with the `OPENZL_BUILD_MODE` variable:

* `none` (default): CMake default build mode controlled by `CMAKE_BUILD_TYPE`
* `dev`: debug build with asserts enabled and ASAN / UBSAN enabled
* `dev-nosan`: debug build with asserts enabled
* `opt`: optimized build with asserts disabled
* `opt-asan`: optimized build with asserts disabled and ASAN / UBSAN enabled
* `dbgo`: optimized build with asserts enabled
* `dbgo-asan`: optimized build with asserts enabled and ASAN / UBSAN enabled

> [!CAUTION]
> When switching between build modes, make sure to purge the CMake cache and re-configure the build. For instance,
> `cmake --fresh -DOPENZL_BUILD_MODE=dev-nosan ..`

For ASAN / UBSAN, ensure that `libasan` and `libubsan` are installed on the machine.

#### Editor Integration

OpenZL ships with settings to configure VSCode to work with the CMake build system. To enable it install two extensions:

1. `cmake-tools`
2. `clangd` (or any other C++ language server that works with `compile_commands.json`)

**Important:** For proper C++ language server support, you need to generate `compile_commands.json`:

The preferred method is to use the CMake Tools extension command "`CMake: Configure`".

If it doesn't work, or is too difficult to setup, you can use the manual setup:

```bash
mkdir -p cmakebuild
cmake -B cmakebuild -DOPENZL_BUILD_TESTS=ON -DCMAKE_EXPORT_COMPILE_COMMANDS=ON .
cp cmakebuild/compile_commands.json .
```

**When to regenerate:**

* After cloning the repository (first-time setup)
* When adding/removing source files
* When modifying `CMakeLists.txt`

#### CMake Variables

* `CMAKE_C_COMPILER` = Set the C compiler for Op