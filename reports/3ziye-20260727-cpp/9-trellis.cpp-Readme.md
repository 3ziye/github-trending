# trellis.cpp

A standalone, **GGML-based C++** implementation of Microsoft's
[TRELLIS.2-4B](https://huggingface.co/microsoft/TRELLIS.2-4B) image-to-3D pipeline:
background removal, image conditioning, the three flow transformers, the VAE decoders,
mesh extraction and UV-textured GLB export — all in native C++/GGML with no Python at
runtime. Optionally driven end-to-end from a text prompt with
[stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp) producing the
input image.

```
./build/trellis-cli assets/goblin.png out/goblin.glb      # image -> UV-textured GLB (atlas + PBR)
python tools/render_glb.py out/goblin.glb out/view.png    # quick multi-view render
```

Prebuilt binaries for Linux and Windows (Vulkan, ROCm, CUDA) are published on the
[releases page](../../releases). Serves as the `trellis` backend of
[Lemonade](https://github.com/lemonade-sdk/lemonade).

## Quick start

New here? **Trellis Studio** is a one-command install that auto-detects your GPU
runtime (CUDA / ROCm / Vulkan), downloads the server + weights, and gives you a
drag-an-image → 3D desktop app with an interactive preview and a saved gallery.

```bash
# Linux (x86-64)
curl -fsSL https://raw.githubusercontent.com/pwilkin/trellis.cpp/main/install/install.sh | bash
```
```powershell
# Windows (x64), in PowerShell
irm https://raw.githubusercontent.com/pwilkin/trellis.cpp/main/install/install.ps1 | iex
```

See [**Trellis Studio (desktop app)**](#trellis-studio-desktop-app) below for what it
does and how to use it, or [`docs/getting-started.md`](docs/getting-started.md) for the
full walkthrough and installer options.

## Showcase

Seven image→3D reconstructions produced end-to-end by trellis.cpp **v0.4.3** on a
single Radeon 8060S (all res-1024 cascade, seed 42, ~300K faces, 2048² atlas; the
GLBs and their Z-Image-Turbo source images live in
[`assets/showcase/`](assets/showcase/)):

<p>
<a href="assets/showcase/axe/axe_quad4k.png"><img src="assets/showcase/axe/axe_quad4k.png" width="49%"></a>
<a href="assets/showcase/chest/chest_quad4k.png"><img src="assets/showcase/chest/chest_quad4k.png" width="49%"></a>
<a href="assets/showcase/cottage/cottage_quad4k.png"><img src="assets/showcase/cottage/cottage_quad4k.png" width="49%"></a>
<a href="assets/showcase/drone/drone_quad4k.png"><img src="assets/showcase/drone/drone_quad4k.png" width="49%"></a>
<a href="assets/showcase/golem/golem_quad4k.png"><img src="assets/showcase/golem/golem_quad4k.png" width="49%"></a>
<a href="assets/showcase/knight/knight_quad4k.png"><img src="assets/showcase/knight/knight_quad4k.png" width="49%"></a>
<a href="assets/showcase/racer/racer_quad4k.png"><img src="assets/showcase/racer/racer_quad4k.png" width="49%"></a>
</p>

Each grid is a 4096×4096 four-view capture — front / right / back / left at 75°
elevation, 2048² per view — made with
[`tools/mv_preview/render_quad.js`](tools/mv_preview/render_quad.js), a headless
Playwright driver around Google's `<model-viewer>`: it serves
`tools/mv_preview/quad.html`, loads the GLB into a 2×2 grid of viewers, waits for
auto-framing to settle, captures each view via `toBlob`, and
[`stitch_quad.py`](tools/mv_preview/stitch_quad.py) assembles the final grid.

## Trellis Studio (desktop app)

**Trellis Studio** is the standalone desktop app (built with [Tauri](https://tauri.app))
for anyone who wants image→3D without touching the command line. The one-command
installer above auto-detects your GPU runtime, downloads the matching
`trellis-server` build plus the ~16.5 GB of weights, and installs the app; on launch
it starts and supervises the server for you, so the whole flow is drag-image →
click → rotate the result.

<p align="center">
<img src="assets/trellis-studio.png" width="92%" alt="Trellis Studio — drop an image, generate a textured 3D model, preview it interactively">
</p>

**Using it:**

1. **Add an image** — drag-and-drop onto the drop zone, click to browse, or paste
   from the clipboard.
2. **Set options** (optional) — resolution (512 light / 1024 cascade / 1536 high),
   seed, background removal (auto / birefnet / threshold), and UV unwrap
   (xatlas / box). Defaults match the CLI.
3. **Generate 3D** — this takes a few minutes; a live stage line shows progress.
4. **Inspect** — rotate and zoom in the interactive preview (Google's three.js-based
   `<model-viewer>`); **Reset view** re-frames the camera and **Save GLB…** exports
   the model.
5. **Reuse** — every result is kept in a local **gallery** (IndexedDB): click a
   thumbnail to reload its model, input image, and settings — even after restarting
   the app.

The **Settings** panel (gear icon) points the app at a different models directory,
GPU index, or port; the models directory, backend, and server binary come from the
`config.json` the installer writes. Because the UI is a plain web bundle you can also
skip the app entirely and open it in a browser against a `trellis-server` you started
yourself — see [`docs/getting-started.md`](docs/getting-star