# kimodo.cpp

GGML/C++ implementation of NVIDIA's Kimodo text-to-motion model.

## Status

The five released Kimodo motion checkpoints accept either a UTF-8 prompt or a
precomputed LLM2Vec embedding and generate local rotations plus root
translations on CPU or Vulkan:

- SMPL-X RP v1: 22 joints
- SOMA RP/SEED v1.1: the predicted compact 30-joint control skeleton
- G1 RP/SEED v1: 34 Unitree G1 joints

NVIDIA's Python API expands SOMA's predicted 30 joints to a relaxed-hand
77-joint presentation skeleton. The native API currently returns the 30 joints
the model actually predicts. The text encoder uses eight-layer Vulkan chunks by
default; set `KIMODO_TEXT_LAYER_CHUNK=1..32` to tune VRAM use.

Included: checked GGUF loading, safetensors conversion, DDIM sampling, C/C++
APIs, conditioned multi-prompt transitions, CPU/Vulkan parity tests,
skeleton-only GLB export, selective LLM2Vec quantisation, divergence reporting,
and local generation/comparison viewers. General constraint input, 77-joint
SOMA expansion, skinned-mesh GLB export, and motion-denoiser quantisation are
not implemented yet.

## Build and test on Linux

Install a C++23 compiler, CMake 3.25+, Ninja, Python 3 with the Hugging Face
CLI (`pip install huggingface_hub`), and the Vulkan loader/headers for Vulkan
support. GGML is a pinned Git submodule:

```sh
git submodule update --init --recursive
scripts/download_gguf_weights.sh --output "$PWD" --model soma-rp-v1.1
cmake --preset debug
cmake --build --preset debug
ctest --preset debug
```

The standard test suite requires the local motion GGUF, text bundle, and
fixtures. It never downloads weights by itself. `release`, `asan-ubsan`, and
`fuzz` presets are also available.

Nix is optional and provides these dependencies reproducibly:

```sh
nix develop path:. --command cmake --preset debug
nix develop path:. --command cmake --build --preset debug
```

For sanitizer work:

```sh
nix develop path:. --command cmake --preset asan-ubsan
nix develop path:. --command cmake --build --preset asan-ubsan
nix develop path:. --command env \
  LD_LIBRARY_PATH="$PWD/build/asan-ubsan/ggml/src:$PWD/build/asan-ubsan/ggml/src/ggml-vulkan:$LD_LIBRARY_PATH" \
  ASAN_OPTIONS=detect_leaks=0:abort_on_error=1 UBSAN_OPTIONS=print_stacktrace=1 \
  ctest --preset asan-ubsan --output-on-failure
```

Leak detection is disabled because Vulkan loader/driver allocations are global
to the process. The GGUF parser fuzzer requires Clang.

## API

`include/kimodo/kimodo_capi.h` is the C API. Model loading checks the motion
GGUF and text model before inference. The text model can be a monolithic GGUF
beside `tokenizer.gguf` or the legacy component directory. Use
`kimodo_generate_embedding` for
4096 F32 values or `kimodo_generate` for text. Both return the selected model's
root translations and local XYZW rotations; query the joint count from the
result rather than assuming a fixed skeleton.

## Demo

After building the debug preset and downloading the native GGUF bundle:

```sh
go run ./demo -addr 0.0.0.0:8094
```

Open `http://localhost:8094`. The left sidebar contains the prompt and a
persistent history plus motion-model and text-encoder-quantization selectors;
choosing a previous animation restores its prompt and encoder choice for a new
generation. Every successful animation also writes a standalone
`animation.glb` beside its raw streams, for example
`demo-output/<animation-id>/animation.glb`. It contains the selected animated
node hierarchy (no mesh), ready to copy into a Three.js project. It is also
available from `/api/animations/<animation-id>/animation.glb` while the demo
is running.

The demo keeps all 32 layers of its default Q8 text encoder in VRAM for maximum
throughput, while executing them as bounded eight-layer GGML graphs. Its 10 GiB
residency ceiling makes the larger BF16 reference stream in bounded groups on a
16 GiB GPU. Library and command-line callers retain the lower-memory eight-layer
default; set `KIMODO_TEXT_LAYER_CHUNK=32` for residency and optionally set
`KIMODO_TEXT_RESIDENT_LIMIT_MIB` to enforce a VRAM-safe bundle-size ceiling.
The demo reuses one native worker while the selected motion model and text
quantization remain unchanged, preserving both weight sets across requests.
Profiling controls, measurements, and the next optimization targets are in
[`docs/PROFILING.md`](docs/PROFILING.md).

Quantisation comparisons produced by the workflow in
[`docs/QUANTIZATION.md`](docs/QUANTIZATION.md) can be opened at
`http://localhost:8094/compare`. Supply their parent directory with the demo's
`--comparisons` option. The comparison view overlays every variant on a shared
timeline and provides world-space and root-position-aligned modes.

## Weights

Ready-to-run native GGML weights are published under the Hugging Face
`LocalAI-io` organisation (not GitHub's `localai-org`). The reusable
[Llama-3-Kimodo-GGML](https://huggingface.co/LocalAI-io/Llama-3-Kimodo-GGML)
text encoder is separate from the four redistributable motion