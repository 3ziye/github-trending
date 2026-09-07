# NoGraphicsAPI

`NoGraphicsAPI` is an experimental Vulkan 1.4 implementation of the ideas in Sebastian Aaltonen's
[*No Graphics API*](https://www.sebastianaaltonen.com/blog/no-graphics-api). It explores how much of
a conventional graphics API disappears when shaders use 64-bit GPU pointers, texture and sampler
descriptors live in application-owned GPU memory, and synchronization describes hazards instead of
resource state.

The Vulkan backend is implemented and exercised by three example applications. Metal support is not
implemented; [the Metal 4 design](docs/metal-porting.md) records the proposed mapping and open issues.

## How it maps to *No Graphics API*

- **GPU pointers replace buffer objects and bindings.** `create_gpu_heap()` returns a raw allocation
  with a GPU address and, for mapped memory, a CPU address. Address-based commands consume
  `GpuRange {gpu, size}` directly, and shaders follow typed 64-bit pointers for vertex fetch and
  arbitrary data structures.
- **Applications own descriptor heaps.** Texture and sampler descriptor heaps are mapped GPU heaps.
  The application chooses slots, writes descriptors through the CPU address, binds the GPU range,
  and passes 32-bit indices to shaders.
- **Root data is one small payload.** A shared C++/Slang structure is copied with
  `vkCmdPushDataEXT` for each draw or dispatch. Its pointer fields are GPU addresses. Unlike the
  blog's GPU-resident, stage-specific roots, graphics stages share one CPU-supplied root.
- **Barriers describe execution and memory hazards.** The public API exposes global stage/access
  barriers, not per-resource transition lists. Normal textures remain in one unified layout.
- **Pipeline binding state stays small.** There are no public buffer objects, descriptor sets,
  descriptor layouts, pipeline layouts, or sampler objects. Viewport, scissor, and exposed
  depth/stencil behavior are command state rather than PSO permutations, while data arrives through the root and descriptor heaps.
- **Submission is explicit and asynchronous.** Applications provide timeline points for reuse and
  deferred destruction. Submitted command buffers are one-shot.

The [design comparison](docs/no-graphics-api-comparison.md) separates faithful mappings, Vulkan-driven
differences, and features that remain outside the prototype.

## Vulkan realization

The backend intentionally creates no `VkDescriptorSetLayout`, `VkDescriptorPool`, `VkDescriptorSet`,
or `VkPipelineLayout`. Its central extensions are:

- `VK_EXT_descriptor_heap` for application-owned resource/sampler heaps and `vkCmdPushDataEXT`;
- `VK_KHR_device_address_commands` for address-based index, indirect, and copy commands;
- `VK_KHR_shader_untyped_pointers` as the descriptor-heap SPIR-V prerequisite;
- `VK_KHR_unified_image_layouts`, when available, to optimize ordinary texture access in
  `VK_IMAGE_LAYOUT_GENERAL`;
- `VK_EXT_mesh_shader` for mesh pipelines and dispatch.

Debug builds enable `VK_EXT_debug_utils` and the Khronos validation layer when available.

Vulkan 1.4 supplies buffer device addresses, timeline semaphores, dynamic rendering,
synchronization2, scalar block layout, and the remaining core features. See
[Vulkan support](docs/vulkan-support.md) for the concise feature and command mapping.

## GPU memory and descriptor heaps

There are no public buffer objects or internal suballocators. Applications own data and descriptor
heaps; optimal-tiled textures use separate GPU-only heaps. The optional utility library provides
application-side data and texture allocation policies.

`GpuRange` is the non-owning address/size view used by commands. Texture and sampler descriptors are
addressed in Slang through the standard heap syntax:

```slang
Texture2D<float4> texture = ResourceDescriptorHeap[texture_index];
SamplerState sampler = SamplerDescriptorHeap[sampler_index];
float4 texel = texture.Sample(sampler, uv);
```

## Shared root ABI

Shared scalar, vector, and matrix types come from `<NoGraphicsAPIUtility/shader_types.h>`. Root
structures are declared once and included by C++ and Slang:

```cpp
struct RootArguments
{
    Vertex* vertices;
    float4x4 mvp;
};
```

On the CPU, pointer fields receive GPU virtual addresses while ordinary values are copied directly:

```cpp
GpuCpuRange<Vertex> vertex_memory = bump_allocator.allocate<Vertex>(vertex_count);
RootArguments root{
    .vertices = vertex_memory.gpu,
    .mvp = mvp,
};
gpu::draw(commands, root, vertex_count);
```

Slang declares the same root as push-constant data and reads both pointer and value fields directly:

```slang
[[vk::push_constant]] ConstantBuffer<RootArguments> root;

Vertex vertex = root.vertices[vertex_id];
float4x4 mvp = root.mvp;
```

The draw or dispatch copies the root bytes immediately through `vkCmdPushDataEXT`; the root does not
need to outlive the call. Shared structures use C layout, and matrix-bearing roots use row-major matrix
layout. Root values must be trivially copyable, have a size divisible by f