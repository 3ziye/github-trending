# skin-tokens.cpp

A C++23/GGML port of
[SkinTokens / TokenRig](https://github.com/VAST-AI-Research/SkinTokens) for
automatic skeleton and skin-weight generation on CPU or Vulkan.

Skin weights say how strongly every mesh vertex follows each bone. Without
them, moving a skeleton does not deform the character surface correctly.
SkinTokens takes a static mesh, predicts a suitable skeleton and its vertex
weights, and writes a portable rigged GLB. 

## Build and install on Linux

Install Git, CMake 3.25 or newer, Ninja, a C++23 compiler,
`nlohmann-json`, and Vulkan headers, loader, and shader compiler. Vulkan can be
disabled with `-DSKINTOKENS_ENABLE_VULKAN=OFF`. From a source checkout:

```sh
git submodule update --init --recursive
cmake -S . -B build/release -G Ninja -DCMAKE_BUILD_TYPE=Release
cmake --build build/release -j
cmake --install build/release --prefix ./dist
```

The `ggml/` submodule is pinned to an official upstream commit. During CMake
configuration, the project copies it into the build directory and applies the
ordered compatibility patches in `patches/ggml/`; the submodule checkout is
never modified. Reconfiguration reuses the prepared copy while the upstream
revision and patch hashes are unchanged. Advanced builds using a GGML tree that
already contains equivalent fixes can pass
`-DSKINTOKENS_APPLY_GGML_PATCHES=OFF`.

The install contains the shared library, C and C++ headers, CLI, GGML runtime,
and enabled dynamic backends. To test from the build tree:

```sh
ctest --test-dir build/release --output-on-failure
./build/release/bin/skintokens-cli inspect models/SkinTokens-GGUF/F16
```

Nix is optional. It supplies the build tools and Vulkan development packages,
but does not replace the normal CMake build:

```sh
nix develop
cmake --preset debug
cmake --build --preset debug -j
ctest --preset debug
```

The sanitizer build is the normal development lane:

```sh
nix develop
cmake --preset asan-ubsan
cmake --build --preset asan-ubsan -j
ctest --preset asan-ubsan
```

## Download the weights

Downloading the converted F16 GGUF bundle is the recommended setup. With the
[Hugging Face CLI](https://huggingface.co/docs/huggingface_hub/guides/cli):

```sh
hf download LocalAI-io/SkinTokens-GGUF \
  --include "F16/*" \
  --local-dir models/SkinTokens-GGUF
```

Use `models/SkinTokens-GGUF/F16` as `MODEL_DIR` in the commands below. The
repository also contains an F32 bundle for numerical parity work; normal
inference should use F16.

## Rig an arbitrary mesh

The standalone path needs only a static `.glb` mesh. It generates the skeleton
and learned skin weights, then stores a one-frame rest pose in the output so it
opens as a conventional skinned glTF asset:

```sh
./build/release/bin/skintokens-cli rig \
  models/SkinTokens-GGUF/F16 \
  character.glb character-rigged.glb \
  --device vulkan
```

The model accepts arbitrary triangle meshes, although—as with any learned
rigging model—results are strongest on shapes resembling its training
distribution. `--postprocess` enables the upstream surface-locality heuristic;
omit it to preserve the raw learned weights exactly.

## Generate skin weights for an existing skeleton

Use `skin` when the armature already exists. A single rigged GLB can provide
both the geometry and static or animated skeleton; its old weights are ignored:

```sh
./build/release/bin/skintokens-cli skin \
  models/SkinTokens-GGUF/F16 \
  character-rigged.glb character-rigged.glb character-reweighted.glb \
  --device vulkan --fit none
```

Alternatively, pass separate mesh and skeleton GLBs. The default `--fit global`
uses a single uniform scale and translation to match vertical extent and centre;
it retains every relative joint position and bone-length ratio. Use `--fit none`
when both files already share coordinates.

`--fit articulated` is an explicitly experimental alternative for recognized
humanoid arm chains. A motion-only skeleton offers two length-exact poses: its
supplied rest pose, and its own first animation frame. This mode measures both
against the mesh surface along the arm bones and keeps whichever actually runs
inside the arms, so a T-pose rig driving a character generated with its arms
lowered adopts the pose the clip already provides. Doing so also makes the bind
pose and frame zero identical, so playback starts without warping the mesh. An
arm chain that still misses is then posed by analytic two-bone inverse
kinematics toward conservative mesh targets, preserving the globally scaled
upper-arm, forearm, and hand lengths exactly. That fallback's invariant follows
the template-skeleton embedding objective in Baran and Popovic's
[Pinocchio](https://www.tonychai.com/072-baran.pdf), but it is deliberately a
small pose stage rather than a copy of Pinocchio's complete LGPL rigging and
weight-generation library. A fuller distance-field embedding implementation can
replace this isolated stage later.

## Status

Safe checkpoint extraction, checked GGUF loading, CPU/Vulkan backend sele