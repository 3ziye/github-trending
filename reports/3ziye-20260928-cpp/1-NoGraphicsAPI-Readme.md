# NoGraphicsAPI

NoGraphicsAPI is a C++20 graphics library designed for the latest **Metal 4** devices and **Vulkan 1.4** devices with
**`VK_EXT_descriptor_heap`**, **`VK_KHR_device_address_commands`**, and **`VK_EXT_mesh_shader`**.
It implements the ideas in Sebastian Aaltonen's [*No Graphics API*](https://www.sebastianaaltonen.com/blog/no-graphics-api)
with GPU pointers, descriptor heaps, and shared Slang shaders.

The goal is to make GPU programming feel more like working with ordinary memory and data structures:
GPU pointers for data, heap indices for textures, and a small argument structure for each draw or dispatch.

Metal 4 and Vulkan are supported native backends. CMake selects Metal on macOS/iOS and Vulkan on Windows/Linux.
Both use the same C++ API and Slang sources. Windows and macOS include windowed examples; Linux currently supports headless use.

## What changes from classic rendering?

A conventional renderer creates buffer objects, describes vertex and resource-binding layouts, and
assembles bindings before drawing. The blog asks how much of this machinery modern bindless hardware
still needs. NoGraphicsAPI makes that alternative data model the foundation of the library:

- **Memory allocation without buffer objects.** Allocate GPU heaps and partition them with an
  application-side allocator. Mapped heaps provide CPU and GPU addresses, so the CPU can write data
  directly. Vertex data, constants, and arbitrary structures are allocations, not separate public buffer types.
- **Typed GPU pointers.** Shaders follow 64-bit pointers stored in shared C++/Slang structures.
  Arrays, pointer arithmetic, and nested data structures work without buffer descriptors or binding slots.
  Vertex shaders fetch their own vertices; there is no vertex-layout declaration.
- **Bindless textures and samplers.** The application owns descriptor heaps and chooses their indices.
  Materials carry those indices as data. Changing materials does not require constructing or rebinding
  per-material descriptor sets.
- **Root arguments instead of binding tables.** Each draw or dispatch receives one small structure
  containing GPU pointers, texture indices, and constants. The CPU and shader share its declaration;
  there are no descriptor-set layouts or pipeline layouts to keep in agreement.
- **Less pipeline-state coupling.** Resource-binding and vertex layouts are absent from pipeline
  creation. Viewport, scissor, and depth/stencil state are set independently, reducing pipeline
  permutations. Rasterization, blending, and attachment formats still belong to pipeline objects.
- **Barriers without resource lists.** Synchronization describes which work produces and consumes
  data, not a list of buffer and image transitions. Applications do not track image layouts.

This is a low-level library: the application still owns allocation policy, resource lifetime, and
GPU synchronization. The optional NoGraphicsAPIUtility library supplies shared shader types, math,
allocators, upload queues, and deferred deletion without making them part of the graphics API.

### What a draw's data looks like

Declare the arguments once in a shared C++/Slang header:

```cpp
struct RootArguments
{
    Vertex* vertices;
    Material* material;
    float4x4 transform;
    uint32 texture_index;
};
```

Fill it with GPU addresses, a transform and a texture-heap index, then pass it to a draw:

```cpp
RootArguments root{
    .vertices = vertex_memory.gpu,
    .material = material_memory.gpu,
    .transform = transform,
    .texture_index = texture_index,
};
gpu::draw(commands, root, vertex_count);
```

With `<NoGraphicsAPI/shader.slang>`, the shader accesses the same data directly:

```slang
GPU_ROOT(RootArguments, root);
Vertex vertex = root.vertices[vertex_id];
Material material = *root.material;
Texture2D<float4> texture = gpu_texture<Texture2D<float4>>(root.texture_index);
```

One deliberate difference from the blog: this implementation copies small root arguments (up to 256 bytes) per command
and shares them across graphics stages, rather than passing separate GPU root pointers for each stage.
See the [design comparison](docs/no-graphics-api-comparison.md) for the remaining differences and
the [shader guide](docs/slang.md) for complete examples.

## Native implementations

Metal 4 supplies native GPU addresses, draw/dispatch commands that accept those addresses, and
`MTLTextureViewPool` for indexed textures. Vulkan supplies the equivalent model through device-address
commands and descriptor heaps. See [Metal implementation](docs/metal-support.md) and
[Vulkan implementation](docs/vulkan-support.md) for how these map to NoGraphicsAPI.

## Hardware requirements

### Metal 4

Requires macOS, iOS or iPadOS 26+ and Apple GPU family 7 or newer with Metal 4.

| Platform | Supported devices |
| --- | --- |
| Mac | Apple silicon Macs (M1 and newer) |
| iPhone | iPhone 12 and newer (A14 and newer) |
| iPad Pro | 2021 and newer (M1 and newer) |
| iPad Air | 20