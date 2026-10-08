# OpenDLSS-NR

A Vulkan reimplementation of NVIDIA's DLSS 5 Neural Rendering network, bit-exact against the original.

The same 71-block Swin / ViT network as DLSS-NR build 310.8.0, running FP8 on the tensor cores. The
intermediates match too, not just the final image: all 75 block boundaries, byte for byte.

`ports/browser-webgpu/` is a second, independent implementation: the same bytes in a browser, with no
tensor cores and no FP8.

**You supply the weights**, as a model directory in the layout described below.

## The network

A U-net of shifted-window transformer blocks with a global ViT at the bottom: 71 blocks over six pooling
levels, FP8 (E4M3) activations with FP16 accumulation, 141 MiB of weights. It is a generative neural rendering
network (NVIDIA's term): it re-renders the frame the engine already drew, generating detail from injected noise
and adjusting tone, structure and skin under a style setting. Input and output are the same resolution; it is not
an upscaler.

![The same frame with neural rendering off (left) and on (right)](docs/images/cowboy-gramps-nr-on.jpg)

*The WebGPU port at 2048x1152, NR off on the left and on on the right. Scene:
[Cowboy Gramps](https://www.blendkit.com/asset-gallery-detail/96dce188-9c9c-4699-a45a-48663fbbbcb7/) by
Muhammed Ismayil, CC0.*

It takes one rendered frame (a low dynamic range proxy of it, three lanes of Gaussian noise, the previous
frame's output reprojected, and five conditioning scalars) and produces four f32 channels per pixel: an RGB
residual and one temporal-blend logit. [docs/network.md](docs/network.md) is the graph in full. NVIDIA
describes the model in its report,
[DLSS 5: Generative Neural Rendering](https://research.nvidia.com/labs/adlr/DLSS5/files/DLSS5_Report.pdf)
([project page](https://research.nvidia.com/labs/adlr/DLSS5/)).

## Build and run

```
powershell -File scripts\fetch_tools.ps1 [-Npm]     # once: tools\ (glslang, Vulkan-Headers, volk, CMake, Ninja)
powershell -File scripts\build.ps1                  # shaders, PTX, build\dlss5vk.exe
powershell -File scripts\fetch_filament.ps1         # once, for the demo: third_party\filament (+ the patch)
powershell -File scripts\build_filament.ps1         # once, for the demo: third_party\filament-install
powershell -File scripts\build_demo.ps1             # build\demo\dlss5-demo.exe
```

```
build\dlss5vk.exe bench   --model <dir> --width 768 --height 768
build\dlss5vk.exe profile --model <dir> --width 768 --height 768   # per-dispatch timings
build\dlss5vk.exe parity  --model <dir> --fixture <dir>            # bit-exactness against a fixture
build\dlss5vk.exe verify  --model <dir> --fixture <dir>            # block-0 kernel-by-kernel bisect
python scripts\ptx\test_fast_divmod.py                             # the PTX divider, over every n < 2^24 (numpy)
```

The demo can be double-clicked. It lists every scene under `build\scenes` in the **Demo scene** dropdown and
starts on the first one, or loads the glTF given on the command line. The model directory is `--model <dir>`,
else `DLSS5VK_MODEL`, else `models\nr` next to this README. See [demo/README.md](demo/README.md) for the
renderer, the keys, the scenes and `view.json`.

## Performance

RTX 4070 SUPER, whole network per frame, minimum over 40 frames. 241 dispatches at every resolution.

| resolution | time |
| --- | --- |
| 768x768 | 2.8 ms |
| 1920x1080 | 7.8 ms |
| 2560x1440 | 12.6 ms |
| 3840x2160 | 29.3 ms |

The GPU alternates between two clock states under sustained load, so medians run a few percent higher. Compare
minima.

## What is here

| Part | Files | Notes |
| --- | --- | --- |
| Host | `src/` (C++20) | Vulkan context, model loading and weight re-layout, kernel wrappers, the network graph, a CPU reference of the arithmetic, the `dlss5vk` tool |
| GLSL kernels | `shaders/` | The reference route: cooperative-matrix FP8 GEMMs, fused 32-channel block, fused QKV + window attention, expert MLP, global attention, elementwise ops. Exact and complete on their own. |
| PTX kernels | `scripts/ptx/` | Python generators emitting PTX for the fast route: `mma.sync` E4M3 with f16 accumulation, cp.async rings, barrier-free chaining through device counters, split-K GEMMs, streamed global attention. Generated into `build/ptx` by the build. |
| Demo | `demo/`, `third_party/filament.patch` | The network inside a Filament (Apache-2.0) frame: Filament patched for per-object motion vectors and a Vulkan interop hook, glTF scenes through gltfio, ImGui controls. |
| WebGPU port | `ports/browser-webgpu/` | The same network in a browser, bit-exact against the same captures, with no tensor core, no FP8, no fusion between blocks and no chaining: the exactness is in the specification, not in the hardware. 72 ms at 512x512 against 2.7 ms here. |

Not implemented: DLSS-SR, which is a different network. The temporal path is implemented, but in the demo: the
network's history input lanes and its per-pixel blend logit drive a reprojected feedback loop
([docs/fra