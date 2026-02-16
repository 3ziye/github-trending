<p align="center">
  <img src="mystralnative.jpg" alt="Mystral Native.js" width="600" />
</p>

<p align="center">
  <a href="https://discord.gg/jUYC9dMbu5"><img src="https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&logoColor=white" alt="Discord" /></a>
  <a href="https://github.com/mystralengine/mystralnative/releases"><img src="https://img.shields.io/github/v/release/mystralengine/mystralnative?label=Release" alt="Release" /></a>
  <a href="https://github.com/mystralengine/mystralnative/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT License" /></a>
</p>

# Mystral Native.js

**Run JavaScript/TypeScript games natively with WebGPU.** Mystral Native.js is a lightweight runtime that lets you write games using familiar Web APIs (WebGPU, Canvas, Audio, fetch) and run them as native desktop applications on macOS, Windows, and Linux.

Think of it as "Electron for games" but without Chromium — just your game code, a JS engine, and native WebGPU rendering.

> [!NOTE]
> Mystral Native.js is in **early alpha**. The core features work — execute JS against WebGPU, Canvas 2D, Web Audio, and fetch — with runtimes available for **macOS**, **Windows**, and **Linux**. Embedding is available for **iOS** and **Android**, with a future goal of console support.
> To see a production build, check out the [Sponza demo on itch.io](https://mystraldev.itch.io/sponza-in-webgpu-mystral-engine).

## Quick Start

### Option 1: Install via CLI (Recommended)

**macOS / Linux:**

```bash
curl -fsSL https://mystralengine.github.io/mystralnative/install.sh | bash
```

**Windows (PowerShell):**

```powershell
irm https://mystralengine.github.io/mystralnative/install.ps1 | iex
```

This detects your platform, downloads the latest release, installs to `~/.mystral/` (or `$HOME\.mystral\` on Windows), and adds `mystral` to your PATH. Then run the examples:

```bash
# macOS / Linux
cd ~/.mystral
mystral run examples/triangle.js
mystral run examples/mystral-helmet.js  # GLTF loading demo
```

```powershell
# Windows (PowerShell)
cd $HOME\.mystral
mystral run examples\triangle.js
mystral run examples\mystral-helmet.js  # GLTF loading demo
```

### Option 2: Download Prebuilt Binary

Download the latest release for your platform from the [releases page](https://github.com/mystralengine/mystralnative/releases):

| Platform | Download |
|----------|----------|
| macOS (Apple Silicon) | `mystral-macOS-arm64-v8-dawn.zip` |
| macOS (Intel) | `mystral-macOS-x64-v8-dawn.zip` |
| Windows | `mystral-windows-x64-v8-dawn.zip` |
| Linux | `mystral-linux-x64-v8-dawn.zip` |

```bash
unzip mystral-macOS-arm64-v8-dawn.zip
cd mystral-macOS-arm64-v8-dawn
./mystral run examples/triangle.js
```

### Option 3: Build from Source

```bash
git clone https://github.com/mystralengine/mystralnative.git
cd mystralnative

# Install bun if you don't have it
curl -fsSL https://bun.sh/install | bash

# Download dependencies
bun install
bun run deps:download

# Configure with V8 + Dawn (recommended)
cmake -B build \
  -DMYSTRAL_USE_V8=ON \
  -DMYSTRAL_USE_DAWN=ON \
  -DMYSTRAL_USE_QUICKJS=OFF \
  -DMYSTRAL_USE_WGPU=OFF

# Build
cmake --build build --parallel

# Run an example
./build/mystral run examples/triangle.js
```

## What Can You Build?

Here's a complete "Hello Triangle" — the traditional first GPU program:

```javascript
// hello-triangle.js
const adapter = await navigator.gpu.requestAdapter();
const device = await adapter.requestDevice();
const context = canvas.getContext("webgpu");
const format = navigator.gpu.getPreferredCanvasFormat();
context.configure({ device, format });

const shader = device.createShaderModule({
  code: `
    @vertex fn vs(@builtin(vertex_index) i: u32) -> @builtin(position) vec4f {
      var pos = array<vec2f, 3>(
        vec2f( 0.0,  0.5),
        vec2f(-0.5, -0.5),
        vec2f( 0.5, -0.5)
      );
      return vec4f(pos[i], 0.0, 1.0);
    }

    @fragment fn fs() -> @location(0) vec4f {
      return vec4f(1.0, 0.5, 0.2, 1.0); // orange
    }
  `,
});

const pipeline = device.createRenderPipeline({
  layout: "auto",
  vertex: { module: shader, entryPoint: "vs" },
  fragment: { module: shader, entryPoint: "fs", targets: [{ format }] },
});

function render() {
  const encoder = device.createCommandEncoder();
  const pass = encoder.beginRenderPass({
    colorAttachments: [{
      view: context.getCurrentTexture().createView(),
      clearValue: { r: 0.1, g: 0.1, b: 0.1, a: 1 },
      loadOp: "clear",
      storeOp: "store",
    }],
  });
  pass.setPipeline(pipeline);
  pass.draw(3);
  pass.end();
  device.queue.submit([encoder.finish()]);
  requestAnimationFrame(render);
}
render();
```

Save it and run:

```bash
mystral run hello-triangle.js
```

You'll see an orange triangle on a dark background — rendered natively via WebGPU with no browser involved.

## Running Examples

```bash
# Basic WebGPU triangle
mystral run examples/triangle.js

# 3D rotating cube
mystral run examples/simple-cube.js

# 