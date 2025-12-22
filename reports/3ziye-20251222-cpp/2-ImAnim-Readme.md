# ImAnim

**Animation Engine for [Dear ImGui](https://github.com/ocornut/imgui)**

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/soufianekhiat/ImAnim)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](../LICENSE)

![ImAnimDemo_Hero_1 0 0](https://github.com/user-attachments/assets/a9e7931c-7e31-4585-80dc-9ac93664ec3e)

ImAnim brings modern animation capabilities to ImGui applications. Write smooth UI animations with minimal code.

## Version 1.0.0 - First Official Release

This is the first stable release of ImAnim, featuring a complete animation toolkit for Dear ImGui.

```cpp
// Animate anything in one line
float alpha = iam_tween_float(id, channel, hovered ? 1.0f : 0.5f, 0.3f, ease, policy, dt);
```

## Why ImAnim?

- **Immediate-mode friendly** - Works naturally with ImGui's paradigm
- **Zero dependencies** - Only requires Dear ImGui
- **Large easing collection** - 30+ easing functions including spring physics
- **Perceptual color blending** - OKLAB and OKLCH
- **Responsive layouts** - Anchor-relative animations that survive window resizing

## Features at a Glance

| Category | Capabilities |
|----------|-------------|
| **Tweens** | Float, Vec2, Vec4, Int, Color with crossfade/cut/queue policies |
| **Clips** | Timeline keyframes, looping, callbacks, chaining, stagger, variations |
| **Easing** | Quad to Bounce presets, cubic-bezier, steps, spring physics, per-axis |
| **Paths** | Bezier curves, Catmull-Rom splines, path morphing, text along paths |
| **Transforms** | Position, rotation, scale with rotation modes |
| **Procedural** | Oscillators, shake, wiggle, Perlin/Simplex noise |
| **Colors** | Gradients, style interpolation, OKLAB/OKLCH blending |
| **Advanced** | Layering/blending, resolved tweens, drag feedback, scroll animation |
| **Tools** | Debug inspector, profiler, save/load, memory management |

## Quick Integration

**Step 1:** Copy `im_anim.h` and `im_anim.cpp` to your project.

**Step 2:** Add two lines after `ImGui::NewFrame()`:

```cpp
ImGui::NewFrame();

// Add these two lines
iam_update_begin_frame();
iam_clip_update(ImGui::GetIO().DeltaTime);

// Your UI code...
```

**Step 3:** Animate! Here's a hover effect:

```cpp
bool hovered = ImGui::IsItemHovered();
float scale = iam_tween_float(
    ImGui::GetID("btn"), ImHashStr("scale"),
    hovered ? 1.1f : 1.0f, 0.2f,
    iam_ease_preset(iam_ease_out_back),
    iam_policy_crossfade,
    ImGui::GetIO().DeltaTime
);
```

That's it. No build system changes, no external dependencies.

## Debug helper

* Timeline for clips with tooltip helpers:
![ImAnimDemo_XukMAvrwhw](https://github.com/user-attachments/assets/cb821e95-fba9-478d-90fe-ebfc710abf62)

* Support for delayed start:
![ImAnimDemo_2fQKeGBaLG](https://github.com/user-attachments/assets/452d3818-93f3-42e0-8683-9d963178c3f5)

## Building Examples

### Windows

Open `examples/ImAnim_vs2022_Win64.sln` in Visual Studio 2022 and select a configuration:

| Configuration | Backend |
|---------------|---------|
| `Release_Win32_DX11` | Win32 + DirectX11 |
| `Release_GLFW_OpenGL3` | GLFW + OpenGL3 |
| `Release_SDL2_OpenGL3` | SDL2 + OpenGL3 |
| `Release_ImPlatform` | ImPlatform abstraction |

Debug configurations are also available for each backend.

### Linux / macOS

Each backend has its own Makefile:

```bash
cd examples/glfw_opengl3
make

# or
cd examples/sdl2_opengl3
make
```

## Documentation

Comprehensive guides for every ImAnim feature, organized by category. Each doc includes code examples and API references.

### Getting Started
- [Integration Guide](integration.md) - Add ImAnim to your project
- [Quick Start](quickstart.md) - Get running in 5 minutes

### Core Animation
- [Tweens](tweens.md) - Immediate-mode animation
- [Clips](clips.md) - Timeline-based keyframe animation
- [Easing](easing.md) - All 30+ easing functions

### Motion & Paths
- [Motion Paths](motion-paths.md) - Animate along curves
- [Path Morphing](path-morphing.md) - Interpolate between paths
- [Text Along Paths](text-along-paths.md) - Curved text rendering
- [Transforms](transforms.md) - 2D transform animation

### Effects
- [Stagger](stagger.md) - Cascading element animations
- [Text Stagger](text-stagger.md) - Per-character text effects
- [Oscillators](oscillators.md) - Continuous periodic motion
- [Shake & Wiggle](shake-wiggle.md) - Feedback and organic motion
- [Noise](noise.md) - Perlin/Simplex procedural animation

### Colors & Styles
- [Gradients](gradients.md) - Color gradient animation
- [Style Interpolation](style-interpolation.md) - Animated theme transitions
- [Per-Axis Easing](per-axis-easing.md) - Different easing per component

### Advanced Features
- [Variations](variations.md) - Per-loop parameter changes
- [Layering](layering.md) - Blend multiple animations
- [Resolved Tweens](resolved-tweens.md) - Dynamic target computation
- [Anchors](anchors.md) - Resize-aware animation
- [Drag Feedback](drag-feedback.md) - Animated drag operations
- [Sc