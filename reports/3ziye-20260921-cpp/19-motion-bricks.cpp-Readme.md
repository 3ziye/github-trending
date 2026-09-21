# motion-bricks.cpp

A C++23/GGML port of NVIDIA MotionBricks for CPU and Vulkan inference, with a
stable C ABI suitable for PureGo.

The released batch-one G1 inference path is implemented end to end: strict
GGUF loading, root/duration planning, pose-token prediction, VQ decoding,
418/414/413 feature conversion, style alignment, and skeletal animation
output. CPU and Vulkan use the same public API and preserve the same duration
and pose-token decisions in the reference suite.

The demo also offers optional native MuJoCo physics driven by **GGML SONIC**,
including Kimodo animation playback, with target/reference/physical skeletons.
The original G1 mode-0 policy passes independent CPU/Vulkan layer parity.
See [SONIC setup, results and limitations](docs/SONIC-GGML.md) and the
[MuJoCo 3.12 upgrade notes](docs/MUJOCO-UPGRADE.md).
The browser sends WebSocket commands and renders buffered server-owned motion;
see [streaming and client QA](docs/STREAMING.md).

## Build

The normal build uses CMake and does not depend on Nix:

```sh
cmake --preset debug
cmake --build --preset debug
ctest --preset debug
```

Configuration downloads and SHA-256-verifies the published 0.73 GB G1 F32
GGUF and style bundles into `generated/` when they are not already present.
The same operation can be run explicitly:

```sh
python scripts/download_gguf_weights.py
```

For an offline or source-only build, preserve an existing local bundle or use
`cmake --preset debug -DMOTIONBRICKS_DOWNLOAD_MODELS=OFF`. The repository and
revision are configurable with `MOTIONBRICKS_MODEL_REPOSITORY` and
`MOTIONBRICKS_MODEL_REVISION`.

On NixOS, enter the reproducible development shell first:

```sh
nix develop
cmake --preset debug
cmake --build --preset debug
ctest --preset debug
```

When the pinned `ggml/` submodule is present, it is included automatically.
The non-neural ABI and validation subset can also be built without GGML:

```sh
cmake -S . -B build/debug -G Ninja -DMOTIONBRICKS_ENABLE_GGML=OFF
```

The Go binding and demo use PureGo to load `libmotionbricks` at runtime; they
do not use cgo or `import "C"`. Once the native shared library has been built,
the Go components therefore need no C compiler and can be built with cgo
explicitly disabled:

```sh
cd demo
CGO_ENABLED=0 go build -o ../build/debug/bin/motionbricks-demo .
```

`CGO_ENABLED=0` is optional but recommended for making this property explicit
in builds and CI. It affects only the Go build—the native C++ library is still
built separately with CMake.

The sanitizer lane is:

```sh
cmake --preset asan-ubsan
cmake --build --preset asan-ubsan
ctest --preset asan-ubsan
```

### SONIC CPU performance

Builds enable GGML runtime CPU selection by default: they package the supported
CPU variants for the target architecture and load the highest-scoring compatible
variant. For CPU-only SONIC inference with `-O3` and profiling symbols:

```sh
cmake --preset sonic-cpu
cmake --build --preset sonic-cpu
ctest --preset sonic-cpu
```

This CPU-only preset uses local SONIC weights and parity fixtures prepared
with the [SONIC setup instructions](docs/SONIC-GGML.md). It builds
`build/sonic-cpu/libmotionbricks.so` and runs backend discovery, API and
one/two-thread parity checks. Set the runtime thread count explicitly; the
[profiling harness](reference/profile_sonic_cpu.py) additionally pins the
process to one or two distinct physical cores with `--cpus`.

On the measured Ryzen 9 7900, an encoder+decoder pair takes about **0.93 ms
on one core** and **0.62 ms on two**. The matched G1-only ONNX Runtime 1.22
comparison takes 1.25 ms / 0.74 ms. Results describe this CPU and workload;
these historical measurements used the single-variant AVX512 build.
The `sonic-cpu-avx512` preset remains available to reproduce those experiments.
See [CPU backend packaging and validation](docs/CPU-BACKENDS.md) for installation
and the explicit `MOTIONBRICKS_CPU_ALL_VARIANTS=OFF` opt-out.
See [measurements and methodology](docs/SONIC-CPU-PROFILE.md),
[the ONNX comparison](docs/SONIC-ONNX-COMPARISON.md), and
[machine-readable summaries](docs/benchmarks/sonic-cpu-2026-09-10.json).

## Current ABI

Start with the [API selection guide](docs/API.md): choose stateless MotionBricks
inference, the optional animation controller, standalone SONIC inference, or
the SONIC/MuJoCo physics controller. The [inference-only C example](examples/inference.c)
uses caller-supplied poses without styles or an agent.

The installed C API uses only fixed-width scalars, pointers, and opaque heap
handles. Callers never reproduce a C or C++ structure layout. All constructors
have matching free functions, and no C++ exception crosses the ABI boundary.

The current CLI can report ABI information:

```sh
./build/debug/bin/motionbricks-cli abi
```

After producing the trusted safetensors intermediates described in
`reference/README.md`, build and inspect an F32 runtime bundle with:

```sh
python scripts/convert_to_gguf.py \
  --safe-directory generated/safe \
